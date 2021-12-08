from django.db import models
from django.core.exceptions import ValidationError
from core.models import ProductColor
from user.models import User
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


class Order(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    basket = models.OneToOneField('Basket', on_delete=models.PROTECT)
    address = models.CharField(max_length=255)
    orderer = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    phone = models.CharField(max_length=25,
                             validators=[validate_phone], )
    payment_type = models.CharField(max_length=255, choices=PaymentType.choices, default=PaymentType.CASH)
    order_status = models.CharField(max_length=255, choices=OrderStatus.choices, default=OrderStatus.OPENED)
    payment_status = models.CharField(max_length=255, choices=PaymentStatus.choices, default=PaymentStatus.WAITING)
    promocode = models.ForeignKey('PromoCode', on_delete=models.PROTECT, null=True, blank=True)
    date_delivered = models.DateField(null=True, blank=True)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
