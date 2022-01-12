from django.db import transaction
from rest_framework import serializers
from api.v1.product.validators import ReviewCreateValidator
from api.v1.services.get_endpoint import get_image_endpoint
from core.models import *
from sprinter_settings import settings
from user.models import BackCall


class BackCallCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackCall
        fields = (
            'id',
            'phone',
            'contact'
        )

