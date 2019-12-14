from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

class UserAdminCustom(UserAdmin):

    list_display = ('email', 'id_no', 'first_name', 'last_name', 'is_staff',)
    list_filter = ('is_staff',)
    # Displayed when updating
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'id_no')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    # Displayed when creating a new user
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email', 'first_name', 'last_name', 'id_no', 'last_name',
                    'password1', 'password2'
                )
            }
        ),
    )
    search_fields = ('email', 'first_name', 'last_name', 'id_no')
    ordering = ('email', 'first_name', 'last_name', 'id_no')
    filter_horizontal = ()

admin.site.register(User, UserAdminCustom)
