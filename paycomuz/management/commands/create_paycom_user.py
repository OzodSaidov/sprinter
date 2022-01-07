# Django
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

# Settings chec

# User model
user_model = get_user_model()


class Command(BaseCommand):
    help = 'Create User for PaycomUz'
    username = 'Paycom'
    username_key = user_model.USERNAME_FIELD
    password = settings.PAYCOM_SETTINGS.get('SECRET_KEY')

    def handle(self, *args, **options):
        try:
            user, _ = user_model.objects.update_or_create(**{self.username_key: self.username})
            print(user)
            print(self.password)
            user.set_password(self.password)
            user.save()
            self.stdout.write(self.style.SUCCESS('Successfully created user'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(str(e)))
