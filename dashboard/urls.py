from django.urls import path
from . import views

urlpatterns = [
    path('', views.analytics, name='analytics'),
    path('', views.analytics, name='analytics'),
    path('run_mapreduce/', views.run_mapreduce_job, name='run_mapreduce'),
    
]

