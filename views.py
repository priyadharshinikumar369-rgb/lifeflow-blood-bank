from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from .models import Inventory


# =====================================
# CHECK ADMIN
# =====================================

def is_admin(user):
    return user.is_authenticated and user.is_staff


# =====================================
# INVENTORY LIST
# =====================================

def inventory_list(request):

    inventory = Inventory.objects.all().order_by('blood_group')

    return render(
        request,
        'inventory/inventory_list.html',
        {
            'inventory': inventory
        }
    )


# =====================================
# ADD INVENTORY
# ADMIN ONLY
# =====================================

@user_passes_test(is_admin, login_url='login')
def inventory_add(request):

    if request.method == 'POST':

        blood_group = request.POST.get('blood_group', '').strip()
        units = request.POST.get('units', '').strip()

        # Check empty fields
        if not blood_group or not units:

            messages.error(
                request,
                'Please fill in all fields.'
            )

            return render(
                request,
                'inventory/inventory_add.html'
            )

        try:

            units = int(units)

            # Check negative units
            if units < 0:

                messages.error(
                    request,
                    'Blood units cannot be negative.'
                )

                return render(
                    request,
                    'inventory/inventory_add.html'
                )

            # Check duplicate blood group
            if Inventory.objects.filter(
                blood_group=blood_group
            ).exists():

                messages.error(
                    request,
                    'This blood group already exists.'
                )

                return render(
                    request,
                    'inventory/inventory_add.html'
                )

            # Create inventory
            Inventory.objects.create(
                blood_group=blood_group,
                units=units
            )

            messages.success(
                request,
                'Blood inventory added successfully!'
            )

            return redirect('inventory_list')

        except ValueError:

            messages.error(
                request,
                'Please enter a valid number of units.'
            )

    return render(
        request,
        'inventory/inventory_add.html'
    )


# =====================================
# EDIT INVENTORY
# ADMIN ONLY
# =====================================

@user_passes_test(is_admin, login_url='login')
def inventory_edit(request, inventory_id):

    item = get_object_or_404(
        Inventory,
        id=inventory_id
    )

    if request.method == 'POST':

        units = request.POST.get('units', '').strip()

        try:

            units = int(units)

            if units < 0:

                messages.error(
                    request,
                    'Blood units cannot be negative.'
                )

                return redirect(
                    'inventory_edit',
                    inventory_id=item.id
                )

            item.units = units
            item.save()

            messages.success(
                request,
                'Inventory updated successfully!'
            )

            return redirect('inventory_list')

        except ValueError:

            messages.error(
                request,
                'Please enter a valid number.'
            )

    return render(
        request,
        'inventory/inventory_edit.html',
        {
            'item': item
        }
    )


# =====================================
# DELETE INVENTORY
# ADMIN ONLY
# =====================================

@user_passes_test(is_admin, login_url='login')
def inventory_delete(request, inventory_id):

    item = get_object_or_404(
        Inventory,
        id=inventory_id
    )

    if request.method == 'POST':

        item.delete()

        messages.success(
            request,
            'Inventory removed successfully!'
        )

    return redirect('inventory_list')