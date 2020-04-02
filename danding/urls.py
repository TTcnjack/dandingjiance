from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path(r'home/', views.home, name='home'),
    path(r'worker/', views.worker, name='worker'),
    path(r'worker_list/', views.worker_list, name='worker_list'),
    path(r'arguments/', views.arguments, name='arguments')

]