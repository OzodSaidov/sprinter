from django.db import models

# Create your models here.
from sprinter_settings.base_models import Base
from mptt.models import TreeForeignKey
from mptt.models import MPTTModel


class Catalog(Base, MPTTModel):
    title = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_catalogs')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class Color(Base):
    title = models.CharField(max_length=255, unique=True)
    icon = models.ImageField(upload_to='photos/color_icons')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class Product(Base):
    catalog = models.ForeignKey('Catalog', on_delete=models.PROTECT, related_name='products')
    color = models.ManyToManyField('Color')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/product')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class ProductParam(Base):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='products')
    param = models.JSONField()


class ProductPrice(Base):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    param = models.ForeignKey('ProductParam', on_delete=models.CASCADE)
    price = models.FloatField()
    available_count = models.PositiveIntegerField()


class PromoCode(Base):
    code = models.CharField(max_length=255, unique=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    product_param = models.ForeignKey('ProductParam', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


