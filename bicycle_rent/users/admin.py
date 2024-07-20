from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class AdminUser(UserAdmin):
    list_display = (
        'username',
        'email',
        'password'
    )


# admin.site.register(User)
admin.site.empty_value_display = 'Не задано'
