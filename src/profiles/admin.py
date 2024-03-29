from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserNet
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

# Register your models here.

class UserNetAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("username", "email", "phone", "first_name", "last_name", "is_staff")


admin.site.register(UserNet, UserAdmin)