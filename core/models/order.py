from django.db import models

# Create your models here.
from common.static_data import PaymentType, OrderStatus, PaymentStatus
from sprinter_settings.base_models import Base


class ProductOrder(Base):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    product_param = models.ForeignKey('ProductParam', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Basket(Base):
    products = models.ManyToManyField('ProductOrder')
    is_active = models.BooleanField(editable=False, default=True)


class Order(Base):
    basket = models.ForeignKey('Basket', on_delete=models.PROTECT)
    payment_type = models.CharField(max_length=255, choices=PaymentType.choices, default=PaymentType.CASH)
    order_status = models.CharField(max_length=255, choices=OrderStatus.choices, default=OrderStatus.OPENED)
    payment_status = models.CharField(max_length=255, choices=PaymentStatus.choices, default=PaymentStatus.WAITING)
    promocode = models.ForeignKey('PromoCode', on_delete=models.PROTECT, null=True, blank=True)
    is_active = models.BooleanField(default=True)