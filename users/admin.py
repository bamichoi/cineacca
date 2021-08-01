from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from . import models
from . import forms


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    model = models.User

    fieldsets = (
        (None, {"fields": ("email", "password", "first_name", "last_name")}),
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
        "is_staff",
        "is_superuser",
    )
    ordering = ("last_name",)

    pass
