from django.shortcuts import render
from inventory.models import Inventory


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def services(request):
    return render(request, 'home/services.html')


def contact(request):
    return render(request, 'home/contact.html')


def home(request):
    inventory = inventory.objects.all()

    return render(request, 'home/home.html', {
        'inventory': inventory
    })

def home(request):
    return render(request, 'home/home.html', {
        'inventory': [
            {'blood_group': 'TEST', 'units': 999}
        ]
    })
# Create your views here.
