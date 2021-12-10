from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from user.models import User
from user.redis import get_basket

