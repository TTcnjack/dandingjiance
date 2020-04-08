from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.home, name='home'),
    # path(r'home/', views.home, name='home'),
    path(r'home/running_rate/', views.running_rate, name='running_rate'),
    path(r'home/break_per/', views.break_per, name='break_per'),
    path(r'home/output/', views.output, name='output'),
    path(r'home/empty_ingot', views.empty_ingot, name='empty_ingot'),
    path(r'home/weak_twist', views.weak_twist, name='weak_twist'),
    path(r'worker/', views.worker, name='worker'),
    path(r'worker_list/', views.worker_list, name='worker_list'),
    path(r'arguments/', views.arguments, name='arguments'),
    path(r'dingding/', views.dingding, name='dingding'),
]
