from django.db import models

# Create your models here.
from sprinter_settings.base_models import Base
from mptt.models import TreeForeignKey
from mptt.models import MPTTModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

from user.models import User


class Catalog(Base, MPTTModel):
    title = models.CharField(max_length=255, unique=True, help_text=_("Название каталога"))
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True,
                            blank=True, related_name='sub_catalogs', help_text=_("К какому каталогу относится этот каталог?"))
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
    color = models.ManyToManyField('Color', blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class ProductImages(Base):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='photos/products')
    is_active = models.BooleanField(default=True)


class ProductParam(Base):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='products')
    param = models.JSONField(default=dict)
    is_important = models.BooleanField(default=False, help_text=_("Этот параметр влияет на цену товара?"))

    def __str__(self):
        return f'{self.product} - {self.param}'


class ProductPrice(Base):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    param = models.ForeignKey('ProductParam', on_delete=models.CASCADE)
    price = models.FloatField()
    available_count = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product} - {self.price}'


class PromoCode(Base):
    code = models.CharField(max_length=255, unique=True)
    product = models.ManyToManyField('Product', blank=True)
    # product_param = models.ForeignKey('ProductParam', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.code}'


class Comment(Base, MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    title = models.TextField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user} - {self.title}'


class Rating(Base):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    rate = models.FloatField(validators=[
        MinValueValidator(0),
        MaxValueValidator(5),
    ])

    def __str__(self):
        return f'{self.user} - {self.product} - {self.rate}'