from django.db import models
from user.models import User
# Create your models here.
from common.static_data import PaymentType, OrderStatus, PaymentStatus
from sprinter_settings.base_models import Base
from user.validators import validate_phone


class ProductOrder(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='productorders')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    product_param = models.ForeignKey('ProductParam', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Basket(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket')
    products = models.ManyToManyField('ProductOrder')
    is_active = models.BooleanField(editable=False, default=True)


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
    is_active = models.BooleanField(default=True)

