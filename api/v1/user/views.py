import re

import pyotp
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.user.serializers import UserMeCreateSerializer
from api.v1.user.services.send_code import send_code

User = get_user_model()


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
    """Verification phone or email"""
    permission_classes = [AllowAny]

    def post(self, request):
        username = self.request.data.get('username')
        if not re.findall(r'\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6}', username) \
                or re.findall(r'^+?998\d{9}$', username):
            return Response({'status': 'bad request'}, status=400)
        if User.objects.filter(username=username).exists():
            return Response({'detail': 'Phone number already exists!'},
                            status=status.HTTP_400_BAD_REQUEST)
        secret = pyotp.random_base32()
        totp = pyotp.TOTP(secret, interval=180)
        otp = totp.now()
        send_code(username, otp)
        return Response({'token': secret}, status=200)
