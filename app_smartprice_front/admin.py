from django.contrib import admin
from .models import *
from .forms import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm

    model = User
    list_display = 'id', 'first_name', 'last_name', 'username'
    search_fields = ('id', 'first_name', 'username')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('Tokken'), {'fields': ('token',)})
    )
    readonly_fields = ('last_login', 'date_joined')