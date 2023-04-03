from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'role')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'name', 'email', 'is_active', 'role'),
        }),
    )
    list_display = ('username', 'name', 'email', 'is_active', 'is_staff', 'role')
    list_filter = ('is_active', 'is_staff', 'role')
    search_fields = ('username', 'name', 'email')


admin.site.register(User, CustomUserAdmin)
