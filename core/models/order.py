from django.db import models
from django.core.exceptions import ValidationError
from core.models import ProductColor
from user.models import User, Address
from common.static_data import PaymentType, OrderStatus, PaymentStatus
from sprinter_settings.base_models import Base
from user.validators import validate_phone
from django.db.models import Sum


class ProductOrder(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='productorders')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    product_param = models.ManyToManyField('ProductParam')
    color = models.ForeignKey(ProductColor, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user} - {self.product}'

    @property
    def price(self):
        """ Return price for this product in given quantity """

        additional_price = self.product.prices.filter(
            param__in=self.product_param.all()).aggregate(additional_price=Sum('price'))
        total_price = self.product.price
        if additional_price.get('additional_price'):
            total_price += additional_price['additional_price']
        return total_price * self.quantity

    @property
    def product_price(self):
        """ Return price of product with some params """
        additional_price = self.product.prices.filter(
            param__in=self.product_param.all()).aggregate(additional_price=Sum('price'))
        product_price = self.product.price
        if additional_price.get('additional_price'):
            product_price += additional_price['additional_price']
        return product_price

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заказ продукт'
        verbose_name_plural = 'Заказы продукты'

    def delete(self, *args, **kwargs):
        """ Do not allow to delete non active product-order. Non-active is for history """

        if not self.is_active:
            raise ValidationError('Can not delete non-active product-order')
        return super().delete(*args, **kwargs)


class Basket(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket')
    products = models.ManyToManyField('ProductOrder')
    is_active = models.BooleanField(editable=False, default=True)

    @property
    def is_empty(self):
        """ Is there any product in basket? """

        if self.products.count() > 0:
            return False
        return True

    @property
    def total_price(self):
        """ Return total price for all products in basket """

        total_price = 0
        for product in self.products.all():
            total_price += product.price
        return total_price

    @property
    def products_count(self):
        """ Return number of products in basket """

        return self.products.count()

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Order(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    basket = models.OneToOneField('Basket', on_delete=models.PROTECT)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    orderer = models.CharField(max_length=255)
    phone = models.CharField(max_length=25,
                             validators=[validate_phone],
                             )
    email = models.EmailField(null=True, blank=True)
    payment_type = models.CharField(max_length=255, choices=PaymentType.choices, default=PaymentType.CASH)
    order_status = models.CharField(max_length=255, choices=OrderStatus.choices, default=OrderStatus.OPENED)
    payment_status = models.CharField(max_length=255, choices=PaymentStatus.choices, default=PaymentStatus.WAITING)
    promocode = models.ForeignKey('PromoCode', on_delete=models.PROTECT, null=True, blank=True)
    date_delivered = models.DateField(null=True, blank=True)
    products_price = models.FloatField(default=0)
    price = models.FloatField(default=0)
    delivery_price = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)

    def save_price(self):
        total_price = 0
        for product in self.basket.products.all():
            price = product.price
            if self.promocode:
                if self.promocode.catalog == product.product.catalog:
                    sale = price * self.promocode.percent / 100
                    price -= sale
            total_price += price
        self.products_price = total_price

        if self.address.region.delivery:
            delivery_price = self.address.region.delivery.delivery_price
            total_price += delivery_price
            self.delivery_price = delivery_price

        self.price = total_price
        self.save()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

