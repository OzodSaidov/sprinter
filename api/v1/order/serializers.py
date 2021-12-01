from rest_framework import serializers
from core.models.order import *


class ProductOrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = [
            'id',
            'user',
            'product',
            'product_param',
            'color',
            'quantity',
        ]


class ProductOrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = [
            'id',
            'user',
            'product',
            'product_param',
            'color',
            'quantity',
        ]


class ProductOrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = [
            'id',
            'user',
            'product',
            'product_param',
            'color',
            'quantity',
        ]


class ProductOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = [
            'id',
            'user',
            'product',
            'product_param',
            'color',
            'quantity',
        ]


class BasketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = [
            'id',
            'user',
            'products',
        ]


class BasketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = [
            'id',
            'user',
            'products',
        ]


class BasketUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = [
            'id',
            'user',
            'products',
        ]


class BasketDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = [
            'id',
            'user',
            'products',
        ]


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'basket',
            'address',
            'orderer',
            'zip_code',
            'phone',
            'payment_type',
            'promocode',
        ]


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'basket',
            'address',
            'orderer',
            'zip_code',
            'phone',
            'payment_type',
            'promocode',
        ]


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'basket',
            'address',
            'orderer',
            'zip_code',
            'phone',
            'payment_type',
            'promocode',
        ]


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'basket',
            'address',
            'orderer',
            'zip_code',
            'phone',
            'payment_type',
            'promocode',
        ]