import os
import uuid

from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Avg
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFit, Adjust
from api.v1.product.services.round_avg import Round
from common.static_data import ProductStatus
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

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'


class Brand(Base):
    title = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='photos/brands', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Product(Base):
    catalog = models.ForeignKey('Catalog', on_delete=models.PROTECT, related_name='products')
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, null=True)
    title = models.CharField('Название', max_length=255)
    description = models.TextField("Описание")
    price = models.FloatField('Цена')
    discount = models.PositiveSmallIntegerField('Скидка', null=True, blank=True,
                                                validators=[MinValueValidator(0), MaxValueValidator(100)])
    old_price = models.FloatField('Старая цена', null=True, blank=True)
    is_active = models.BooleanField('Продукт активен?', default=True)
    is_slider = models.BooleanField('Показывать на слайдере?', default=False)
    is_on_sale = models.BooleanField('На скидке?', default=False)
    is_new = models.BooleanField('Новый?', default=True)
    is_stock = models.BooleanField('Есть в наличии?', default=False)
    status = models.CharField(max_length=255, choices=ProductStatus.choices, default=ProductStatus.IN_STOCK)
    available_quantity = models.PositiveIntegerField('Доступное количество', default=0)

    def __str__(self):
        return f'{self.title}'

    @property
    def rating(self):
        return self.rating_set.all().aggregate(rate=Round(Avg('rate')))['rate']

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductColor(Base):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='colors',
                                null=True, blank=True)
    # product = models.ManyToManyField('Product', related_name='colors')
    color = ColorField()
    title = models.CharField(max_length=255, null=True)

    def __str__(self):
        if self.product:
            return f'{self.title} {self.product.title}'
        return f'{self.title}'

    class Meta:
        verbose_name = 'Цвет продукта'
        verbose_name_plural = 'Цветов продукты'

    # def __str__(self):
    #     return self.title


class ProductImage(Base):

    def get_file_path(self, filename):
        extension = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), extension)
        return os.path.join('photos/products/', filename)

    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    color = models.ForeignKey('ProductColor', on_delete=models.SET_NULL, null=True, related_name='images')
    image = models.ImageField(upload_to=get_file_path,
                              validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])],
                              error_messages={'extension': _('File extension must be jpeg or jpg or png')})
    image_200x200 = ImageSpecField(processors=[Adjust(contrast=1.2, sharpness=1.1), ResizeToFit(200, 200)],
                                   source='image', format='PNG', options={'quality': 90})
    image_320x350 = ImageSpecField(processors=[Adjust(contrast=1.2, sharpness=1.1), ResizeToFit(320, 350)],
                                   source='image', format='PNG', options={'quality': 90})
    image_540x370 = ImageSpecField(processors=[Adjust(contrast=1.2, sharpness=1.1), ResizeToFit(540, 370)],
                                   source='image', format='PNG', options={'quality': 90})
    is_active = models.BooleanField(default=False)
    is_slider = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Картина продукта'
        verbose_name_plural = 'Картинки продукты'


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
        if self.product:
            return f'{self.key} - {self.value} - {self.product.title}'
        return f"{self.key} - {self.value}"

    class Meta:
        verbose_name = 'Параметр продукта'
        verbose_name_plural = 'Параметры продукты'


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

    class Meta:
        verbose_name = 'Цена продукта'
        verbose_name_plural = 'Цены продукты'


class PromoCode(Base):
    code = models.CharField(max_length=255, unique=True)
    catalog = models.ForeignKey('Catalog', on_delete=models.CASCADE)
    percent = models.FloatField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.code}'

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'


class Comment(Base, MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_comments')
    text = models.TextField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    # def __str__(self):
    #     return f'{self.user} - {self.text}'

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'


class Rating(Base):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    review = models.OneToOneField('Review', on_delete=models.SET_NULL, null=True, blank=True)
    rate = models.FloatField(validators=[
        MinValueValidator(0),
        MaxValueValidator(5),
    ], default=0)

    # def __str__(self):
    #     return f'{self.user} - {self.product} - {self.rate}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Review(Base):
    """ Отзыв (Оценка продукта)"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    like = models.CharField('Что понравилось больше всего?', max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class ReviewImage(Base):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='review/',
                              validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])],
                              error_messages={'extension': _('File extension must be jpeg or jpg or png')})

    class Meta:
        verbose_name = 'Файл отзыва'
        verbose_name_plural = 'Файлы отзывов'


class Delivery(Base):
    region = models.OneToOneField('Region', on_delete=models.SET_NULL, null=True)
    delivery_price = models.PositiveIntegerField()
    # date_delivered = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'


class Region(Base):
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
