from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    add_fieldsets = (
        ('Account Info', {
            'fields': ('username', 'password1', 'password2')
        }),

        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),

        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )

    fieldsets = (
        ('Account Info', {
            'fields': ('username', 'password')
        }),

        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),

        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    
    list_display = ('username', 'first_name', 'last_name', 'email')

admin.site.register(CustomUser, CustomUserAdmin)
