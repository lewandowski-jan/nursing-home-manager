from django.urls import path

from . import views

urlpatterns = [
    path('workers', views.workers, name='manager_workers'),
    path('seniors', views.seniors, name='manager_seniors'),
    path('medicines', views.medicines, name='manager_medicines'),
]