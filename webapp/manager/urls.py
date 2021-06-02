from django.urls import path

from . import views

urlpatterns = [
    path('', views.workers, name='manager'),

    path('workers', views.workers, name='manager_workers'),
    path('workers/edit/<int:id>', views.edit_worker, name='manager_edit_worker'),
    path('workers/new_postal', views.new_postal, name='manager_new_postal'),
    path('workers/new_address/<int:postalid>', views.new_address, name='manager_new_address'),
    path('workers/new_worker/<int:addressid>', views.new_worker, name='manager_new_worker'),

    path('seniors', views.seniors, name='manager_seniors'),
    path('seniors/edit/<int:id>', views.edit_senior, name='manager_edit_senior'),
    path('seniors/new_card', views.new_card, name='manager_new_card'),
    path('seniors/new_senior/<int:cardid>', views.new_senior, name='manager_new_senior'),
    
    

    path('medicines', views.medicines, name='manager_medicines'),
    path('medicines/edit/<int:id>', views.edit_medicine, name='manager_edit_medicine'),
    path('medicines/new_medicine', views.new_medicine, name='manager_new_medicine'),
    path('medicines/change_amount/<int:id>', views.medicines_change_amount, name='manager_medicines_change_amount'),
    
    
]