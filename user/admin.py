from django.contrib import admin

from user.models import User


class UserAdminModel(admin.ModelAdmin):
    list_display = ( 'id', 'full_name', 'phone', 'role', )


admin.site.register(User, UserAdminModel)