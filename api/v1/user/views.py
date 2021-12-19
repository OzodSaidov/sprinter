import re
import pyotp
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from api.v1.user.serializers import UserMeCreateSerializer, LoginSerializer, ResetPasswordSerializer, UserSerializer, \
    AddressSerializer, UserMeUpdateSerializer
from api.v1.user.services.send_code import send_code
from api.v1.user.services.utilities import check_session_basket
from django.db import transaction
from user.models import Address
from user.permissions import UserPermission
from django.utils.translation import ugettext as _

User = get_user_model()


class UserMeCreateView(generics.CreateAPIView):
    """User registration"""
    serializer_class = UserMeCreateSerializer
    permission_classes = [AllowAny]

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        sms_code = request.data.get("sms_code")
        token = request.data.get("token")
        if sms_code and token:
            totp = pyotp.TOTP(token, interval=300)
            if totp.verify(sms_code):
                return super(UserMeCreateView, self).post(request, *args, **kwargs)
            return Response({'error': "You entered incorrect or deprecated code"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': "not otp or token"}, status=status.HTTP_400_BAD_REQUEST)


class VerifyAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reset = self.request.query_params.get('reset', False)
        username = self.request.data.get('username', '')
        if not username:
            return Response(dict(username=[_('Required field.')]), status=status.HTTP_400_BAD_REQUEST)
        if re.findall(r'\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6}', username):
            user = User.objects.filter(email=username)
            data = 'email'
        elif re.findall(r'^[+]?998\d{9}$', username):
            username = re.sub('[^0-9]', '', username)
            user = User.objects.filter(phone=username)
            data = 'phone'
        else:
            return Response(dict(detail=_('You entered a phone or email in the wrong format')),
                            status=status.HTTP_400_BAD_REQUEST)

        if reset == 'true':
            if not user.exists():
                return Response(dict(detail=f'The {data} you entered isn’t connected to an account'),
                                status=status.HTTP_404_NOT_FOUND)
        else:
            if user.exists():
                return Response(dict(detail=f'The {data} you entered is connected to another account'),
                                status=status.HTTP_400_BAD_REQUEST)

        secret = pyotp.random_base32()
        totp = pyotp.TOTP(secret, interval=300)
        otp = totp.now()
        send_code(username, otp)
        return Response({'token': secret}, status=200)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = self.request.data.get('username', '')
        password = self.request.data.get('password', '')
        usr = 'phone'
        if not username:
            if not password:
                return Response(dict(username=[_('Required field.')], password=[_('This field cannot be empty.')]),
                                status=status.HTTP_400_BAD_REQUEST)
            return Response(dict(username=[_('Required field.')]), status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response(dict(password=[_('This field cannot be empty.')]), status=status.HTTP_400_BAD_REQUEST)

        if re.findall(r'\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6}', username):
            user = User.objects.filter(email=username)
            usr = 'email'
        elif re.findall(r'^[+]?998\d{9}$', username):
            username = re.sub('[^0-9]', '', username)
            user = User.objects.filter(phone=username)
        else:
            return Response(dict(detail=_('You entered a phone or email in the wrong format')),
                            status=status.HTTP_400_BAD_REQUEST)
        if not user.exists():
            return Response(
                {'detail': f'The {usr} you entered isn’t connected to an account'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        if not user.first().check_password(password):
            return Response({'detail': 'You entered an incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)

        check_session_basket(user=user.first(), request=request)
        serializer = LoginSerializer(user.first())

        # TODO """ Uncomment this when redis will be set in server """
        ##check_session_basket(user=user.last(), request=request)

        return Response(serializer.data)


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
            return Response({"user": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        totp = pyotp.TOTP(token, interval=300)
        if not (code and token):
            if not totp.verify(code):
                return Response({"error": "You entered incorrect or deprecated code"},
                                status=status.HTTP_400_BAD_REQUEST)
            return Response({'error': "Invalid token or code"}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(password)
        user.save()
        return Response({"message": "Password successfully changed"}, status=status.HTTP_200_OK)


class UserMeView(generics.RetrieveAPIView):
    permission_classes = [UserPermission]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserMeUpdateView(generics.UpdateAPIView):
    permission_classes = [UserPermission]
    serializer_class = UserMeUpdateSerializer

    def get_object(self):
        return self.request.user


class AddressListCreateView(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    permission_classes = [UserPermission]

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)


class AddressDeleteView(generics.DestroyAPIView):
    permission_classes = [UserPermission]
    queryset = Address.objects.all()
