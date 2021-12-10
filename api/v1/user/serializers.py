from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.serializers import Serializer

from user.token import MyTokenObtainPairSerializer
from api.v1.user.services.utilities import check_session_basket
User = get_user_model()


class UserMeCreateSerializer(serializers.ModelSerializer):
    refresh_token = serializers.SerializerMethodField(read_only=True)
    access_token = serializers.SerializerMethodField(read_only=True)
    username = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'phone',
            'email',
            'address',
            'zip_code',
            'password',
            'access_token',
            'refresh_token'
        ]

    def get_refresh_token(self, obj):
        return str(self.refresh_token)

    def get_access_token(self, obj):
        return str(self.access_token)

    def create(self, validated_data):
        password = validated_data.pop('password')
        phone = validated_data.get('phone')
        user = User(**validated_data)
        user.username = phone
        user.is_active = True
        user.set_password(password)
        user.save()
        self.refresh_token = MyTokenObtainPairSerializer.get_token(user)
        self.access_token = self.refresh_token.access_token
        check_session_basket(request=self.context.get('request'), user=user)
        return user


class LoginSerializer(Serializer):
    def to_representation(self, instance):
        data = super(LoginSerializer, self).to_representation(instance)
        refresh_token = MyTokenObtainPairSerializer.get_token(instance)
        access_token = refresh_token.access_token
        data['access_token'] = str(access_token)
        data['refresh_token'] = str(refresh_token)
        return data


class ResetPasswordSerializer(Serializer):
    code = serializers.CharField()
    token = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        data["code"] = data["code"].zfill(6)
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'user_ident',
            'first_name',
            'last_name',
            'phone',
            'email',
            'address',
            'zip_code',
        )