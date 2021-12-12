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
    user_id = -1111
    username_key = user_model.USERNAME_FIELD

    def handle(self, *args, **options):
        try:
            print('hi')
            assert settings.PAYCOM_SETTINGS.get('SECRET_KEY') != None
            password = settings.PAYCOM_SETTINGS['SECRET_KEY']
            print('no')
            print(password)
            print(user_model)
            user, _ = user_model.objects.update_or_create(**{self.username_key: self.username, 'id': self.user_id})
            print(user)
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS('Successfully created user'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(str(e)))
