from django.urls import path
from . import views


urlpatterns = [

    # Inventory List
    path(
        '',
        views.inventory_list,
        name='inventory_list'
    ),

    # Add Inventory
    path(
        'add/',
        views.inventory_add,
        name='inventory_add'
    ),

    # Edit Inventory
    path(
        'edit/<int:inventory_id>/',
        views.inventory_edit,
        name='inventory_edit'
    ),

    # Delete Inventory
    path(
        'delete/<int:inventory_id>/',
        views.inventory_delete,
        name='inventory_delete'
    ),

]