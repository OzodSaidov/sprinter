import django_filters
from core.models.order import *


class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = Order
        fields = [
            'order_status',
        ]


class BasketListFilter(django_filters.FilterSet):
    class Meta:
        model = Basket
        fields = [
            'is_active'
        ]