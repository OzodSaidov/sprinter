from django.contrib import admin

from user.models import User


class UserAdminModel(admin.ModelAdmin):
    list_display = ('email', 'phone', 'full_name', 'role', 'id')


admin.site.register(User, UserAdminModel)
