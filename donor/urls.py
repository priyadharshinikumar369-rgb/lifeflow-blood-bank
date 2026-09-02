from django.urls import path
from . import views


urlpatterns = [

    path('', views.donor_list, name='donor_list'),

    path('add/', views.donor_add, name='donor_add'),

    path(
        'delete/<int:donor_id>/',
        views.donor_delete,
        name='donor_delete'
    ),

]