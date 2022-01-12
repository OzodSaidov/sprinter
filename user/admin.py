from django.contrib import admin
from django.contrib.auth.views import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from user.models import Address, BackCall
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
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups'),
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


@admin.register(Address)
class AddressAdminModel(admin.ModelAdmin):
    list_display = ('user', 'address', 'zip_code', 'full_name')


@admin.register(BackCall)
class BackCallAdminModel(admin.ModelAdmin):
    list_display = ('phone', 'contact')