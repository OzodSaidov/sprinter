from rest_framework import serializers

from api.v1.order.validation import ProductOrderValidation
from api.v1.product.serializers import ProductRetrieveSerializer, ColorSerializer, ProductParamSerializer, \
    ProductShortDetailSerializer, ProductImageShortSerializer
from api.v1.user.serializers import AddressSerializer
from core.models import ProductParam, Product, ProductGroup
from core.models.order import *
from django.db import transaction
from django.db.models import Sum, F, When


class ProductOrderListSerializer(serializers.ModelSerializer):
    product = ProductRetrieveSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    price = serializers.ReadOnlyField()
    product_price = serializers.ReadOnlyField()
    product_param = ProductParamSerializer(many=True)

    class Meta:
        model = ProductOrder
        fields = [
            'id',
            'user',
            'product',
            'product_param',
            'color',
            'product_price',
            'quantity',
            'price',
            'is_active',
        ]


class ProductOrderShortSerializer(serializers.ModelSerializer):
    product = ProductShortDetailSerializer(read_only=True)
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ProductOrder
        fields = [
            'id',
            'product',
            # 'color',
            'quantity',
            'image',
        ]

    def get_image(self, obj):
        image = obj.color.images.first()
        if image:
            data = ProductImageShortSerializer(image, many=False, context=self.context).data
            return data['image']
        elif obj.product.images.first():
            data = ProductImageShortSerializer(obj.product.images.first(), many=False, context=self.context).data
            return data['image']
        return []


class ProductOrderCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    product_param = serializers.PrimaryKeyRelatedField(required=False, many=True,
                                                       queryset=ProductParam.objects.all())

    class Meta:
        model = ProductOrder
        fields = [
            'id',
            'user',
            'product',
            'color',
            'product_param',
            'quantity',
        ]

    def validate(self, attrs):
        """ All important params should be chosen. Not important param cannot be chosen.
        Evey important param has a group, only one param from each group can be chosen"""

        product = attrs.get('product')
        validator = ProductOrderValidation(product=product, attrs=attrs)
        validator.validate()

        return attrs

    @transaction.atomic
    def create(self, validated_data):
        user = validated_data.get('user')
        product = validated_data.get('product')
        color = validated_data.get('color')
        product_params = validated_data.pop('product_param', [])
        quantity = validated_data.get('quantity')
        same_product = user.productorders.filter(is_active=True, product=product,
                                                 color=color)
        for param in product_params:
            same_product = same_product.filter(product_param=param)
        if same_product.exists():
            product_order = same_product.last()
            product_order.quantity += quantity
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
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProductOrder
        fields = [
            'id',
            'user',
            'quantity',
        ]

    def update(self, instance, validated_data):
        quantity = validated_data.get('quantity', 0)
        instance.quantity += quantity
        instance.save()

        return instance

    def validate(self, attrs):
        validator = ProductOrderValidation(product=self.instance.product, attrs=attrs)
        validator.validate_quantity()

        return attrs


class ProductOrderDetailSerializer(serializers.ModelSerializer):
    price = serializers.ReadOnlyField()
    product_price = serializers.ReadOnlyField()
    product = ProductRetrieveSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    product_param = ProductParamSerializer(many=True)

    class Meta:
        model = ProductOrder
        fields = [
            'id',
            'product',
            'product_param',
            'color',
            'product_price',
            'quantity',
            'price',

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
    address = AddressSerializer(read_only=True, many=False)

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'basket',
            'address',
            'orderer',
            'email',
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
            'orderer',
            'email',
            'address',
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
            'address',
            'orderer',
            'email',
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
            'email',
            'phone',
            'payment_type',
            'order_status',
            'promocode',
            'price',
            'date_delivered',
        ]


