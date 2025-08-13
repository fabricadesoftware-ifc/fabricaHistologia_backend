from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User, PersonalData, Address

@admin.register(Address)
class AdrressAdmin(admin.ModelAdmin):
    list_display = [
        "city",
        "state",
    ]
    search_fields = [
        "city",
        "state",
    ]
    list_filter = [
        "city",
        "state",
    ]
    fields = [
        "city",
        "state",
    ]
    readonly_fields = ["id"]


@admin.register(PersonalData)
class PersonalDataAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "registration",
        "birth_date",
        "phone",
        "education_level",
        "university",
        "user",
        "address",
    ]
    search_fields = [
        "name",
        "registration",
        "birth_date",
        "phone",
        "education_level",
        "university",
        "user",
        "address",
    ]
    list_filter = [
        "name",
        "registration",
        "birth_date",
        "phone",
        "education_level",
        "university",
        "user",
        "address",
    ]
    fields = [
        "name",
        "registration",
        "birth_date",
        "phone",
        "education_level",
        "university",
        "user",
        "address",
    ]
    readonly_fields = ["id"]
    ordering = ["name"]

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password", "passage_id")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Personal info"),
            {"fields": (["verification_token", "is_verified"])},
        ),
        (
            _("Permissions"),
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "passage_id",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    readonly_fields = ["date_joined", "last_login"]

