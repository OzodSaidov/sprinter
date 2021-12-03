from rest_framework import serializers

from api.v1.product.serializers import ProductRetrieveSerializer, ColorSerializer
from core.models.order import *
from django.db import transaction
from django.db.models import Sum, F, When


class ProductOrderListSerializer(serializers.ModelSerializer):
    product = ProductRetrieveSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    price = serializers.ReadOnlyField()

    class Meta:
        model = ProductOrder
        fields = [
            'id',
            'user',
            'product',
            'product_param',
            'color',
            'quantity',
            'is_active',
            'price',
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
    price = serializers.ReadOnlyField()
    product = ProductRetrieveSerializer(read_only=True)
    color = ColorSerializer(read_only=True)

    class Meta:
        model = ProductOrder
        fields = [
            'id',
            'product',
            'product_param',
            'color',
            'quantity',
            'price'
        ]


class BasketListSerializer(serializers.ModelSerializer):
    products = ProductOrderDetailSerializer(read_only=True, many=True)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Basket
        fields = [
            'id',
            'user',
            'products',
            'is_active',
            'total_price',
        ]


class BasketCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Basket
        fields = [
            'id',
            'user',
            'total_price',
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
    products = ProductOrderDetailSerializer(read_only=True, many=True)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Basket
        fields = [
            'id',
            'user',
            'products',
            'total_price',
        ]


class OrderListSerializer(serializers.ModelSerializer):
    basket = BasketDetailSerializer(read_only=True)
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
            'order_status',
            'promocode',
            'price',
            'date_delivered',
        ]


class OrderCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # basket = BasketDetailSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'basket',
            'user',
            'address',
            'orderer',
            'zip_code',
            'phone',
            'payment_type',
            'price',
            'promocode',
        ]
        read_only_fields = ('price',)


    def validate_basket(self, basket):
        if basket.is_empty:
            raise ValidationError('Basket is empty. Cannot create order')
        return basket

    @transaction.atomic
    def create(self, validated_data):
        """ When order is created, dis-active basket and its products """

        basket = validated_data.get('basket')
        basket.products.all().update(is_active=False)
        basket.is_active = False
        basket.save()

        order = Order(**validated_data)
        order.price = basket.total_price
        order.save()

        return order


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
    basket = BasketDetailSerializer(read_only=True)
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
            'order_status',
            'promocode',
            'price',
            'date_delivered',
        ]