from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid
from common.static_data import UserRoles
from sprinter_settings.base_models import Base
from .validators import validate_phone


class User(AbstractUser, Base):
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    user_ident = models.CharField(max_length=9, unique=True)
    role = models.CharField(max_length=255, choices=UserRoles.choices, default='User')
    phone = models.CharField(max_length=25,
                             unique=True,
                             error_messages={
                                 'unique': _('User with that phone already exists')
                             },
                             validators=[validate_phone], )
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['email', 'phone']

    def __str__(self):
        return self.get_username()

    @property
    def full_name(self):
        return self.get_full_name()

    def save(self, *args, **kwargs):
        if not self.user_ident:
            ident = str(uuid.uuid4().fields[-1])[:9]
            self.user_ident = ident

        if not self.username:
            self.username = self.phone
        super(User, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Address(Base):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=25, validators=[validate_phone])
    zip_code = models.CharField(max_length=9)
    address = models.TextField()
    region = models.ForeignKey('core.Region', on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адресы'


class BackCall(Base):
    phone = models.CharField(max_length=20)
    contact = models.CharField(max_length=255)
    is_answered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - {self.phone}"

    class Meta:
        verbose_name = 'Запрос за звонок'
        verbose_name_plural = 'Запросы на звонки'