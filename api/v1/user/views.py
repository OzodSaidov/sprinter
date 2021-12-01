import re

import pyotp
# from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.user.serializers import UserMeCreateSerializer, LoginSerializer
from api.v1.user.services.send_code import send_code

# User = get_user_model()
from user.models import User


class UserMeCreateView(CreateAPIView):
    """User registration"""
    serializer_class = UserMeCreateSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        sms_code = request.data.get("sms_code")
        token = request.data.get("token")
        if sms_code:
            totp = pyotp.TOTP(token, interval=180)
            if totp.verify(sms_code):
                return super().post(request, *args, **kwargs)
            return Response({'status': "invalid code"}, status=402)

        return Response({'status': "not otp or token"}, status=401)


class PhoneVerifyAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone = self.request.data.get('phone')
        phone = re.sub('[^0-9]', '', phone)
        if len(phone) != 12:
            return Response({'status': 'bad request'}, status=400)
        if User.objects.filter(phone__iexact=phone).exists():
            return Response({'detail': 'Phone number already exists!'},
                            status=status.HTTP_400_BAD_REQUEST)
        secret = pyotp.random_base32()
        totp = pyotp.TOTP(secret, interval=180)
        otp = totp.now()
        send_code(phone, otp)
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
                    print(user.first())
                    serializer = LoginSerializer(user.first())
                    print('DONE!')
                    return Response(serializer.data)
                else:
                    print('FAIL!')
                    return Response({'error': 'Incorrect data'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(
                    {'user': 'Not found'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response({'error': 'Incorrect data'}, status=status.HTTP_400_BAD_REQUEST)
