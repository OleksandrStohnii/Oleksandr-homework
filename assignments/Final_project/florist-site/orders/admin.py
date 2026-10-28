from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "event_type", "event_date", "status", "created_at")
    list_filter = ("status", "event_type")
    search_fields = ("name", "phone")
    list_editable = ("status",)