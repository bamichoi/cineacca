from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from . import models
from . import forms

admin.site.unregister(Group)


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    model = models.User

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    "email_verified",
                )
            },
        ),
        (
            _("Personal info"),
            {"fields": ("school", "biography", "account_type", "avatar")},
        ),
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

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "account_type"),
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("account_type", "school")

    list_display = (
        "email",
        "first_name",
        "last_name",
        "school",
        "account_type",
        "email_verified",
        "is_staff",
        "is_superuser",
    )
    ordering = ("last_name",)
