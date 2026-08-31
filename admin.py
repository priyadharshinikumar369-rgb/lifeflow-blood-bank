from django.contrib import admin
from .models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'blood_group',
        'units',
    )

    list_filter = (
        'blood_group',
    )

    search_fields = (
        'blood_group',
    )