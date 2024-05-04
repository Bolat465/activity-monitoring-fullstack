from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('city', 'workplace', 'date_birth', 'phone', 'sex', 'address', 'family_status', 'profile_picture')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'classes': ('wide',),
            'fields': ('city', 'workplace', 'date_birth', 'phone', 'sex', 'address', 'family_status', 'profile_picture'),
        }),
    )

