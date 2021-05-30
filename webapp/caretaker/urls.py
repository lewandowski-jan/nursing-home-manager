from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.seniors, name='caretaker'),
    path('seniors', views.seniors, name='caretaker_seniors'),
    path('medicines', views.medicines, name='caretaker_medicines'),
    path('seniors/healthcard/<int:id>', views.seniors_healthcard, name='caretaker_seniors_healthcard'),
    path('medicines/minus/<int:id>', views.medicines_minus, name='caretaker_medicines_minus'),
    path('medicines/plus/<int:id>', views.medicines_plus, name='caretaker_medicines_plus'),
]