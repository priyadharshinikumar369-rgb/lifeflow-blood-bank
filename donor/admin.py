from django.contrib import admin
from .models import Donor


@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'age',
        'blood_group',
        'phone',
        'last_donation_date',
    )

    list_filter = (
        'blood_group',
    )

    search_fields = (
        'name',
        'phone',
        'blood_group',
    )