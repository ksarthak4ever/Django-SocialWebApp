from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.models import User


class UserAdmin(BaseUserAdmin): #making Users in admin pannel look a bit neat
    fieldsets = (
        (None, {'fields': ('name', 'phone_number', 'email', 'password')}),
        ('Permissions', {'fields': (
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'name', 'phone_number', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('email', 'phone_number')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)