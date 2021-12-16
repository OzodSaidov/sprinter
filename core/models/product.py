from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Avg

from api.v1.product.services.round_avg import Round
from sprinter_settings.base_models import Base
from mptt.models import TreeForeignKey
from mptt.models import MPTTModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from colorfield.fields import ColorField
from user.models import User


class Catalog(Base, MPTTModel):
    title = models.CharField(max_length=255, unique=True, help_text=_("Название каталога"))
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True,
                            blank=True, related_name='sub_catalogs',
                            help_text=_("К какому каталогу относится этот каталог?"))
    image = models.ImageField(upload_to='photos/catalogs', null=True, blank=True)
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
    discount = models.PositiveSmallIntegerField('Скидка', null=True, blank=True)
    old_price = models.FloatField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_slider = models.BooleanField(default=False)
    is_on_sale = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)
    available_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.title}'

    @property
    def rating(self):
        return self.rating_set.all().aggregate(rate=Round(Avg('rate')))['rate']


class ProductColor(Base):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='colors',
                                null=True, blank=True)
    color = ColorField()
    title = models.CharField(max_length=255, null=True)

    def __str__(self):
        if self.product.title:
            return f'{self.title} {self.product.title}'
        return f'{self.title}'


class ProductImage(Base):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    color = models.ForeignKey('ProductColor', on_delete=models.SET_NULL, null=True, related_name='images')
    image = models.ImageField(upload_to='photos/products')
    is_active = models.BooleanField(default=False)


class ProductGroup(Base):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.title}'


class ProductParam(Base):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='params')
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
        if self.product.title:
            return f'{self.key} - {self.value} - {self.product.title}'
        return f"{self.key} - {self.value}"


class ProductPrice(Base):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='prices')
    param = models.OneToOneField('ProductParam', on_delete=models.CASCADE, related_name='prices')
    price = models.FloatField()
    available_count = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product} - {self.price}'

    def save(self, *args, **kwargs):
        """ Эту модель можно использовать только для параметров влияющих на цену
        (ProductParam.is_important)"""

        if not self.param.is_important:
            raise ValidationError('Невозможно создать для такого параметра')
        return super().save(*args, **kwargs)


class PromoCode(Base):
    code = models.CharField(max_length=255, unique=True)
    product = models.ManyToManyField('Product', blank=True)
    # product_param = models.ForeignKey('ProductParam', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.code}'


class Comment(Base, MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_comments')
    text = models.TextField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    # def __str__(self):
    #     return f'{self.user} - {self.text}'


class Rating(Base):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    review = models.OneToOneField('Review', on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='product_rating')
    rate = models.FloatField(validators=[
        MinValueValidator(0),
        MaxValueValidator(5),
    ], default=0)

    # def __str__(self):
    #     return f'{self.user} - {self.product} - {self.rate}'


class Review(Base):
    """ Отзыв (Оценка продукта)"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    like = models.CharField('Что понравилось больше всего?', max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)


class ReviewImage(Base):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='review/',
                              validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])],
                              error_messages={'extension': _('File extension must be jpeg or jpg or png')})
