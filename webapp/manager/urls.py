from django.urls import path

from . import views

urlpatterns = [
    path('', views.workers, name='manager'),
    path('workers', views.workers, name='manager_workers'),
    path('seniors', views.seniors, name='manager_seniors'),
    path('medicines', views.medicines, name='manager_medicines'),
    path('medicines/add/<int:id>', views.medicines_add, name='manager_medicines_add'),
]