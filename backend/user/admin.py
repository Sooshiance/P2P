from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = ("username", "is_phone", "is_email", "is_superuser")
    filter_horizontal = ()
    list_filter = ("is_phone", "is_email", "is_superuser")
    fieldsets = ()
    search_fields = ("username",)


admin.site.register(User, UserAdmin)
