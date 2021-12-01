from rest_framework import serializers
from core.models.order import *
from django.db import transaction

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
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

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

    @transaction.atomic
    def create(self, validated_data):
        user = validated_data.get('user')
        product = validated_data.get('product')
        color = validated_data.get('color')
        product_params = validated_data.pop('product_param')
        quantity = validated_data.get('quantity')
        same_product = user.productorders.filter(is_active=True, product=product,
                                                 color=color, product_param__in=product_params)
        if same_product.exists():
            product_order = same_product.last()
            product_order.quantity = quantity
        else:
            product_order = ProductOrder.objects.create(**validated_data)
            product_order.product_param.set(product_params)
        product_order.save()
        basket = user.basket.filter(is_active=True)
        if basket.exists():
            basket = basket.last()
        else:
            basket = Basket.objects.create(user=user)
        basket.products.add(product_order)
        basket.save()
        return product_order


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
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Basket
        fields = [
            'id',
            'user',
        ]

    def validate(self, attrs):
        user = attrs.get('user')
        if user.basket.filter(is_active=True):
            raise ValidationError('Корзина уже существует')
        return attrs


class BasketUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = [
            'id',
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