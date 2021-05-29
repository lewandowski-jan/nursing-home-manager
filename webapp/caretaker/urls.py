from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('seniors', views.seniors, name='caretaker_seniors'),
    path('medicines', views.medicines, name='caretaker_medicines'),
]