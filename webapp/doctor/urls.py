from django.urls import path

from . import views

urlpatterns = [
    path('', views.seniors, name='doctor'),
    path('seniors', views.seniors, name='doctor_seniors'),
    path('seniors/card/<int:id>', views.senior_card, name='doctor_senior'),
    path('seniors/edit_card/<int:id>', views.edit_card, name='doctor_edit_card'),
    path('seniors/assigned_medicines/<int:id>', views.assigned_medicines, name='doctor_assigned_medicines'),
    path('seniors/assigned_medicine/remove/<int:id>', views.assigned_medicine_remove, name='doctor_assigned_medicine_remove'),
    path('seniors/assigned_medicine/add/<int:id>', views.assigned_medicine_add, name='doctor_assigned_medicine_add'),
]