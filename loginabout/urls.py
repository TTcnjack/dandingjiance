from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.login, name='login'),
    path(r'home_ajax/', views.home_ajax, name='home_ajax'),

]