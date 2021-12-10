import re

import pyotp
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.user.serializers import UserMeCreateSerializer, LoginSerializer, ResetPasswordSerializer, UserSerializer
from api.v1.user.services.send_code import send_code
from api.v1.user.services.utilities import check_session_basket

User = get_user_model()
from django.db import transaction

# from user.models import User


class UserMeCreateView(CreateAPIView):
    """User registration"""
    serializer_class = UserMeCreateSerializer
    permission_classes = [AllowAny]

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        sms_code = request.data.get("sms_code")
        token = request.data.get("token")
        if sms_code:
            totp = pyotp.TOTP(token, interval=300)
            if totp.verify(sms_code):
                return super(UserMeCreateView, self).post(request, *args, **kwargs)
            return Response({'status': "invalid code"}, status=402)

        return Response({'status': "not otp or token"}, status=401)


class VerifyAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reset = self.request.query_params.get('reset', False)
        username = self.request.data.get('username')
        is_email = re.findall(r'\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6}', username)
        is_phone = re.findall(r'^[+]?998\d{9}$', username)
        user_not_found = Response({'user': 'Not found!'}, status=status.HTTP_404_NOT_FOUND)
        user_exists = Response({'user': 'Already exists!'}, status=status.HTTP_400_BAD_REQUEST)
        error = Response({'error': 'Incorrect data!'})

        if reset == 'true':
            if is_email:
                if not User.objects.filter(email=username).exists():
                    return user_not_found
            elif is_phone:
                username = re.sub('[^0-9]', '', username)
                if not User.objects.filter(phone=username).exists():
                    return user_not_found
            else:
                return error
        else:
            if is_email:
                if User.objects.filter(email=username).exists():
                    return user_exists
            elif is_phone:
                username = re.sub('[^0-9]', '', username)
                if User.objects.filter(phone=username).exists():
                    return user_exists
            else:
                return error

        secret = pyotp.random_base32()
        totp = pyotp.TOTP(secret, interval=300)
        otp = totp.now()
        send_code(username, otp)
        return Response({'token': secret}, status=200)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = self.request.data.get('username')
        password = self.request.data.get('password')
        if re.findall(r'\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6}', username):
            user = User.objects.filter(email=username)
        elif re.findall(r'^[+]?998\d{9}$', username):
            username = re.sub('[^0-9]', '', username)
            user = User.objects.filter(phone=username)
        else:
            return Response({'error': 'Incorrect data'}, status=status.HTTP_400_BAD_REQUEST)
        if username and password:
            if user.exists():
                if user.first().check_password(password):
                    check_session_basket(user=user.first(), request=request)
                    serializer = LoginSerializer(user.first())
                    return Response(serializer.data)
                else:
                    return Response({'error': 'Incorrect data'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(
                    {'user': 'Not found'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response({'error': 'Incorrect data'}, status=status.HTTP_400_BAD_REQUEST)


class UserResetPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        token = data["token"]
        code = data["code"]
        password = data["password"]
        phone = data["username"]
        code = code.zfill(6)
        phone = re.sub('[^0-9]', '', phone)
        user = User.objects.filter(phone=phone).first()
        if not user:
            return Response({"phone": "not found"}, status=status.HTTP_404_NOT_FOUND)
        totp = pyotp.TOTP(token, interval=300)
        if code and token:
            if totp.verify(code):
                user.set_password(password)
                user.save()
                return Response({"password_updated": "ok"}, status=status.HTTP_200_OK)
            return Response({"error": "You entered incorrect or deprecated code"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': "invalid token"}, status=status.HTTP_400_BAD_REQUEST)


class UserMeView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
