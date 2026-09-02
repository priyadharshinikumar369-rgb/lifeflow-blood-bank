from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from donor.models import Donor
from inventory.models import Inventory


# ===============================
# DASHBOARD VIEW
# ===============================

@login_required(login_url='login')
def dashboard(request):

    # Total Donors
    donors_count = Donor.objects.count()

    # Total Blood Units
    blood_units = sum(
        item.units
        for item in Inventory.objects.all()
    )

    # Number of Blood Groups
    blood_groups = Inventory.objects.count()

    # Send data to dashboard
    context = {
        'donors_count': donors_count,
        'blood_units': blood_units,
        'blood_groups': blood_groups,
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )