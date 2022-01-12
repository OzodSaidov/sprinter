from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import *


class BackCallCreateView(generics.CreateAPIView):
    serializer_class = BackCallCreateSerializer
    permission_classes = [AllowAny,]
