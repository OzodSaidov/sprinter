from django.contrib import admin
from django.contrib.auth.views import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from user.models import Address
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'email', 'user_ident')


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreateForm

    fieldsets = (
        (_('User information'), {
            'fields': ('user_ident', 'username', 'first_name', 'last_name', 'phone', 'email', 'password')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions'),
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'phone', 'email', 'password1', 'password2',),
        }),
    )

    save_on_top = True
    readonly_fields = ('user_ident', 'username')


# @admin.register(User)
# class UserAdminModel(admin.ModelAdmin):
#     list_display = ('username', 'email', 'full_name', 'role', 'group', 'id')
#
#     def group(self, user):
#         groups = []
#         for group in user.groups.all():
#             groups.append(group.name)
#         return ' '.join(groups)
#
#     group.short_description = 'Groups'


@admin.register(Address)
class AddressAdminModel(admin.ModelAdmin):
    list_display = ('user', 'address', 'zip_code', 'full_name')

# admin.site.unregister(User)
# admin.site.register(Address, AddressAdminModel)
# admin.site.register(User, UserAdminModel)
