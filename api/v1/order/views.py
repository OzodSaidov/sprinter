import re

import pyotp
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.user.serializers import UserMeCreateSerializer
from api.v1.user.services.send_code import send_code
from api.v1.order.serializers import *
from core.models.order import *


class ProductOrderListApiView(ListAPIView):
    """ List of products in basket """

    serializer_class = ProductOrderListSerializer
    queryset = ProductOrder.objects.all()


class ProductOrderCreateApiView(CreateAPIView):
    """ Create product to add to basket """

    serializer_class = ProductOrderCreateSerializer
    queryset = ProductOrder.objects.all()


class ProductOrderUpdateApiView(CreateAPIView):
    """ Update product to add to basket """

    serializer_class = ProductOrderCreateSerializer
    queryset = ProductOrder.objects.all()


class ProductOrderDetailApiView(RetrieveAPIView):
    """ Detail of product in basket """

    serializer_class = ProductOrderDetailSerializer
    queryset = ProductOrder.objects.all()


class ProductOrderDestroyApiView(CreateAPIView):
    """ Delete product from basket """

    queryset = ProductOrder.objects.all()


class BasketListApiView(ListAPIView):
    """ List of baskets """

    serializer_class = BasketListSerializer
    queryset = Basket.objects.all()


class BasketCreateApiView(CreateAPIView):
    """ Create basket """

    serializer_class = BasketCreateSerializer
    queryset = Basket.objects.all()


class BasketUpdateApiView(UpdateAPIView):
    """ Update basket """

    serializer_class = BasketUpdateSerializer
    queryset = Basket.objects.all()


class BasketDetailApiView(RetrieveAPIView):
    """ Detail of baskets """

    serializer_class = BasketDetailSerializer
    queryset = Basket.objects.all()


class BasketDestroyApiView(DestroyAPIView):
    """ Delete basket """

    queryset = Basket.objects.all()


class OrderCreateApiView(CreateAPIView):
    """ Create order """

    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()


class OrderListApiView(ListAPIView):
    """ List of orders """

    serializer_class = OrderListSerializer
    queryset = Order.objects.all()


class OrderUpdateApiView(UpdateAPIView):
    """ Update order """

    serializer_class = OrderUpdateSerializer
    queryset = Order.objects.all()


class OrderDetailApiView(RetrieveAPIView):
    """ Detail of order """

    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()


class OrderDestroyApiView(DestroyAPIView):
    """ Destroy order """

    queryset = Order.objects.all()