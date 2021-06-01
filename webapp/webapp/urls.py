from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('caretaker/', include('caretaker.urls')),
    path('manager/', include('manager.urls')),
    path('admin/', admin.site.urls),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
]