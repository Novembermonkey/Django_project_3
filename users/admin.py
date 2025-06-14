from django.contrib import admin
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'is_active', 'is_staff', 'is_superuser', 'date_joined']
    list_filter = ['is_staff', 'is_superuser']

    fieldsets = [
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('date_joined',)}),
        ('Profile Picture', {'fields': ('profile_pic',)})
    ]
    add_fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password')}
        ),
    ]
    search_fields = ['email',]
    ordering = ['email',]

admin.site.register(CustomUser, CustomUserAdmin)