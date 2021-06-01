from django.urls import path

from . import views

urlpatterns = [
    path('', views.workers, name='manager'),
    path('workers', views.workers, name='manager_workers'),
    path('seniors', views.seniors, name='manager_seniors'),
    path('medicines', views.medicines, name='manager_medicines'),
    path('medicines/change_amount/<int:id>', views.medicines_change_amount, name='manager_medicines_change_amount'),
    path('seniors/new_card', views.new_card, name='manager_new_card'),
    path('seniors/new_senior/<int:cardid>', views.new_senior, name='manager_new_senior'),
    path('medicines/edit/<int:id>', views.edit_medicine, name='manager_edit_medicine'),
]