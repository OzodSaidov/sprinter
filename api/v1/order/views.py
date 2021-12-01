from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from api.v1.order.filters import OrderFilter
from api.v1.order.serializers import *
from core.models.order import *


class ProductOrderListApiView(ListAPIView):
    """ List of products in basket """

    serializer_class = ProductOrderListSerializer

    def get_queryset(self):
        return ProductOrder.objects.filter(user=self.request.user)


class ProductOrderCreateApiView(CreateAPIView):
    """ Create product to add to basket """

    serializer_class = ProductOrderCreateSerializer
    queryset = ProductOrder.objects.all()


class ProductOrderUpdateApiView(CreateAPIView):
    """ Update product to add to basket """

    serializer_class = ProductOrderCreateSerializer

    def get_queryset(self):
        return ProductOrder.objects.filter(user=self.request.user)


class ProductOrderDetailApiView(RetrieveAPIView):
    """ Detail of product in basket """

    serializer_class = ProductOrderDetailSerializer

    def get_queryset(self):
        return ProductOrder.objects.filter(user=self.request.user)


class ProductOrderDestroyApiView(CreateAPIView):
    """ Delete product from basket """

    def get_queryset(self):
        return ProductOrder.objects.filter(user=self.request.user)


class BasketListApiView(ListAPIView):
    """ List of baskets """

    serializer_class = BasketListSerializer

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user)


class BasketCreateApiView(CreateAPIView):
    """ Create basket """

    serializer_class = BasketCreateSerializer
    queryset = Basket.objects.all()


class BasketUpdateApiView(UpdateAPIView):
    """ Update basket """

    serializer_class = BasketUpdateSerializer

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user)


class BasketDetailApiView(RetrieveAPIView):
    """ Detail of baskets """

    serializer_class = BasketDetailSerializer

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user)


class BasketDestroyApiView(DestroyAPIView):
    """ Delete basket """

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user)


class OrderCreateApiView(CreateAPIView):
    """ Create order """

    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()


class OrderListApiView(ListAPIView):
    """ List of orders """

    serializer_class = OrderListSerializer
    filterset_class = OrderFilter

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderUpdateApiView(UpdateAPIView):
    """ Update order """

    serializer_class = OrderUpdateSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderDetailApiView(RetrieveAPIView):
    """ Detail of order """

    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderDestroyApiView(DestroyAPIView):
    """ Destroy order """

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)