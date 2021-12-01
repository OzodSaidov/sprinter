from django.contrib.auth import get_user_model

from rest_framework import serializers

from user.token import MyTokenObtainPairSerializer

User = get_user_model()


class UserMeCreateSerializer(serializers.ModelSerializer):
    refresh_token = serializers.SerializerMethodField(read_only=True)
    access_token = serializers.SerializerMethodField(read_only=True)
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
        user = User(**validated_data)
        user.is_active = True
        user.set_password(password)
        user.save()
        self.refresh_token = MyTokenObtainPairSerializer.get_token(user)
        self.access_token = self.refresh_token.access_token
        return user
