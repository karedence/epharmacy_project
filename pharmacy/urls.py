from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('search/', views.medicine_search, name='medicine_search'),
    path('dashboard/', views.pharmacist_dashboard, name='pharmacist_dashboard'),
    path('medicine/', views.medicine_list, name='medicine_list'),
    path('medicine/create/', views.medicine_create, name='medicine_create'),
    path('medicine/<int:pk>/update/', views.medicine_update, name='medicine_update'),
    path('medicine/<int:pk>/delete/', views.medicine_delete, name='medicine_delete'),
    path('dashboard/analytics/', views.dashboard, name='dashboard'),
    path('pharmacies/', views.pharmacy_list, name='pharmacy_list'),
    path('pharmacies/create/', views.pharmacy_create, name='pharmacy_create'),
    path('pharmacies/<int:pk>/update/', views.pharmacy_update, name='pharmacy_update'),
    path('pharmacies/<int:pk>/delete/', views.pharmacy_delete, name='pharmacy_delete'),
    
 
]

