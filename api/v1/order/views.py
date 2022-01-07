from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from api.v1.order.filters import OrderFilter, BasketListFilter
from api.v1.order.serializers import *
from core.models.order import *
from rest_framework.views import APIView
from django.http import JsonResponse


class ProductOrderListApiView(ListAPIView):
    """ List of products in basket """
    permission_classes = [AllowAny]
    serializer_class = ProductOrderListSerializer

    def get_queryset(self):
        return ProductOrder.objects.filter(user=self.request.user)


class ProductOrderCreateApiView(CreateAPIView):
    """ Create product to add to basket """

    serializer_class = ProductOrderCreateSerializer
    queryset = ProductOrder.objects.all()


class ProductOrderUpdateApiView(UpdateAPIView):
    """ Update product to add to basket """

    serializer_class = ProductOrderUpdateSerializer

    def get_queryset(self):
        return ProductOrder.objects.filter(user=self.request.user, is_active=True)


class ProductOrderDetailApiView(RetrieveAPIView):
    """ Detail of product in basket """

    serializer_class = ProductOrderDetailSerializer

    def get_queryset(self):
        return ProductOrder.objects.filter(user=self.request.user)


class ProductOrderDestroyApiView(DestroyAPIView):
    """ Delete product from basket """

    def get_queryset(self):
        return ProductOrder.objects.filter(user=self.request.user, is_active=True)


class BasketListApiView(ListAPIView):
    """ List of baskets """

    serializer_class = BasketListSerializer
    filterset_class = BasketListFilter

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

    permission_classes = [AllowAny]
    serializer_class = OrderListSerializer
    filterset_class = OrderFilter

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, is_active=True).order_by('-created_at')


class OrderUpdateApiView(UpdateAPIView):
    """ Update order """

    serializer_class = OrderUpdateSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, order_status=OrderStatus.OPENED,
                                    payment_status=PaymentStatus.WAITING, is_active=True)


class OrderDetailApiView(RetrieveAPIView):
    """ Detail of order """

    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, is_active=True)


class OrderDestroyApiView(DestroyAPIView):
    """ Destroy order """

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        order_id = kwargs.get('pk', 0)
        order = Order.objects.filter(id=order_id, payment_status=PaymentStatus.WAITING, is_active=True)
        if order.exists():
            order.update(is_active=False)
            return HttpResponse(status=200)
        return HttpResponse(status=404)


class CurrentBasketApiView(RetrieveAPIView):
    """ Get current basket """
    serializer_class = BasketDetailSerializer

    def get_object(self):
        basket = self.request.user.basket.filter(is_active=True)
        return basket.last()


class CurrentBasketProductNumberApiView(APIView):
    """ Get number of products in basket """

    def get(self, request):
        basket = request.user.basket.filter(is_active=True)
        count = dict(number_of_products=0)
        if basket.exists():
            count['number_of_products'] = basket.last().products_count
        return JsonResponse(count)


class CurrentBasketProductsListApiView(ListAPIView):
    """ Get current basket's product-orders """

    serializer_class = ProductOrderShortSerializer

    def get_queryset(self):
        user = self.request.user
        basket = user.basket.filter(is_active=True).last()
        if basket:
            return basket.products.all().order_by('-created_at')
        return []