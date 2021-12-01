from django.db import models

# Create your models here.
from sprinter_settings.base_models import Base
from mptt.models import TreeForeignKey
from mptt.models import MPTTModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator

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


class Color(Base):
    title = models.CharField(max_length=255, unique=True)
    icon = models.ImageField(upload_to='photos/color_icons')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class Product(Base):
    catalog = models.ForeignKey('Catalog', on_delete=models.PROTECT, related_name='products')
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, null=True, blank=True)
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
    name = models.CharField(max_length=255)
    property = models.CharField(max_length=255)
    is_important = models.BooleanField(default=False, help_text=_("Этот параметр влияет на цену товара?"))

    def __str__(self):
        return f'{self.name} - {self.property}'


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


class Review(Base):
    """ Отзыв (Оценка продукта)"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    rating = models.ForeignKey('Rating', on_delete=models.SET_NULL, null=True)
    like = models.CharField('Что понравилось больше всего?', max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)


class ReviewAttachment(Base):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='review/',
                              validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])],
                              error_messages={'extension': _('File extension must be jpeg or jpg or png')})
