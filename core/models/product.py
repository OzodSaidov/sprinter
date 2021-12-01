from django.db import models

# Create your models here.
from sprinter_settings.base_models import Base
from mptt.models import TreeForeignKey
from mptt.models import MPTTModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from colorfield.fields import ColorField
from user.models import User


class Catalog(Base, MPTTModel):
    title = models.CharField(max_length=255, unique=True, help_text=_("Название каталога"))
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True,
                            blank=True, related_name='sub_catalogs',
                            help_text=_("К какому каталогу относится этот каталог?"))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class Brand(Base):
    title = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='photos/brands')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class Product(Base):
    catalog = models.ForeignKey('Catalog', on_delete=models.PROTECT, related_name='products')
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class ProductColor(Base):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='colors')
    color = ColorField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'

class ProductImages(Base):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='photos/products')
    is_active = models.BooleanField(default=True)


class ProductGroup(Base):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.title}'


class ProductParam(Base):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='products')
    group = models.ForeignKey('ProductGroup', on_delete=models.SET_NULL, null=True, blank=True)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    is_important = models.BooleanField(default=False, help_text=_("Этот параметр влияет на цену товара?"))

    @property
    def has_group(self):
        """ If product params does not belong to any group, it is static """

        if self.group:
            return True
        return

    def __str__(self):
        return f'{self.key} - {self.value}'


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
