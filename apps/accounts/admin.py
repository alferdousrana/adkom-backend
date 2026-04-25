from django.contrib import admin

from .models import Address, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "full_name", "phone", "created_at")
    search_fields = ("user__username", "user__email", "full_name", "phone")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "full_name", "city", "is_default", "created_at")
    list_filter = ("is_default", "city", "created_at")
    search_fields = ("user__username", "user__email", "full_name", "phone", "city")