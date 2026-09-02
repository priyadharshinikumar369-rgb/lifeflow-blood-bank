from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from .models import Donor


# ==================================
# CHECK ADMIN
# ==================================

def is_admin(user):
    return user.is_authenticated and user.is_staff


# ==================================
# DONOR LIST
# ==================================

def donor_list(request):

    donors = Donor.objects.all().order_by('-id')

    return render(
        request,
        'donor/donor_list.html',
        {
            'donors': donors
        }
    )


# ==================================
# ADD DONOR
# ADMIN ONLY
# ==================================

@user_passes_test(is_admin, login_url='login')
def donor_add(request):

    if request.method == 'POST':

        name = request.POST.get('name', '').strip()
        age = request.POST.get('age', '').strip()
        blood_group = request.POST.get('blood_group', '').strip()
        phone = request.POST.get('phone', '').strip()
        address = request.POST.get('address', '').strip()
        last_donation_date = request.POST.get(
            'last_donation_date', ''
        ).strip()

        if not name or not age or not blood_group or not phone or not address:

            messages.error(
                request,
                'Please fill in all required fields.'
            )

            return render(
                request,
                'donor/donor_add.html'
            )

        try:

            age = int(age)

            Donor.objects.create(
                name=name,
                age=age,
                blood_group=blood_group,
                phone=phone,
                address=address,
                last_donation_date=last_donation_date or None
            )

            messages.success(
                request,
                'Donor added successfully!'
            )

            return redirect('donor_list')

        except ValueError:

            messages.error(
                request,
                'Please enter a valid age.'
            )

    return render(
        request,
        'donor/donor_add.html'
    )


# ==================================
# DELETE DONOR
# ADMIN ONLY
# ==================================

@user_passes_test(is_admin, login_url='login')
def donor_delete(request, donor_id):

    donor = get_object_or_404(
        Donor,
        id=donor_id
    )

    if request.method == 'POST':

        donor.delete()

        messages.success(
            request,
            'Donor removed successfully!'
        )

    return redirect('donor_list')