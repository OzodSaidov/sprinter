from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid
from common.static_data import UserRoles
from sprinter_settings.base_models import Base
from .validators import validate_phone


class User(AbstractUser, Base):
    user_ident = models.CharField(max_length=9, unique=True)
    address = models.TextField()
    zip_code = models.CharField(max_length=9)
    role = models.CharField(max_length=255, choices=UserRoles.choices, default='User')
    phone = models.CharField(max_length=25,
                             unique=True,
                             error_messages={
                                 'unique': _('User with that phone already exists')
                             },
                             validators=[validate_phone], )
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.get_username()

    @property
    def full_name(self):
        return self.get_full_name()

    def save(self, *args, **kwargs):
        ident = str(uuid.uuid4().fields[-1])[:9]
        self.user_ident = ident
        super(User, self).save(*args, **kwargs)

""""
class User()
class Colors()
class Catalog()
class Product():
     sovun
class ProductParams()

class ProductQuantity()
    product
    params
    quantity
    price
    
class OrderAttachments():
    user 
    M2M ProductQuantity
    
    
class Order()
    user
    orderattahcment
    
    
class Comment()
class Rating()
class Promocode()
class Price()
    product
    param
    price = '233'

"""