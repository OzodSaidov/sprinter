from django.contrib import admin

from core.models import Basket
from user.models import User
from django import forms


class UserAdminModel(admin.ModelAdmin):
    list_display = ('username', 'email', 'full_name', 'role', 'group', 'id')

    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ' '.join(groups)
    group.short_description = 'Groups'


admin.site.register(User, UserAdminModel)
