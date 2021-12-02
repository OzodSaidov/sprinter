from django.db import models
from django.core.exceptions import ValidationError

import sprinter_settings.settings
from core.models import ProductColor
from user.models import User
# Create your models here.
from common.static_data import PaymentType, OrderStatus, PaymentStatus
from sprinter_settings.base_models import Base
from user.validators import validate_phone
from django.db.models import F, Sum

class ProductOrder(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='productorders')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    product_param = models.ManyToManyField('ProductParam')
    color = models.ForeignKey(ProductColor, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user} - {self.product}'

    def delete(self, *args, **kwargs):
        """ Do not allow to delete non active product-order. Non-active is for history """

        if not self.is_active:
            raise ValidationError('Can not delete non-active product-order')
        return super().delete(*args, **kwargs)


class Basket(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket')
    products = models.ManyToManyField('ProductOrder')
    is_active = models.BooleanField(editable=False, default=True)

    # def save(self, *args, **kwargs):
    #     """ Only one active basket allowed """
    #
    #     if Basket.objects.filter(is_active=True).exists():
    #         raise ValidationError('Basket already exists')
    #     return super().save(*args, **kwargs)
    @property
    def is_empty(self):
        """ Is there any product in basket? """

        if self.products.count() > 0:
            return False
        return True

    @property
    def total_price(self):
        """ Return total price for all products in basket """
        products = self.products.annotate(price=F('product__price') * F("quantity"))
        total_price = products.aggregate(price=Sum('price'))
        return total_price.get('price')


class Order(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    basket = models.ForeignKey('Basket', on_delete=models.PROTECT)
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
