from django.urls import path

from . import views

urlpatterns = [
    path('', views.seniors, name='doctor'),
    path('seniors', views.seniors, name='doctor_seniors'),
    path('seniors/card/<int:id>', views.senior_card, name='doctor_senior'),
    path('seniors/edit', views.edit_card, name='doctor_edit_card'),
    path('seniors/edit_medicines', views.edit_medicines, name='doctor_edit_medicines'),
]