from django.urls import path

from . import views

urlpatterns = [
    path('workers', views.manager_workers, name='manager_workers'),
]