from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('home/', views.home, name="home"),
    path('home/<int:pk>', views.detail, name="detail"),
    path('listenrollees/', views.list_of_enrollees, name="list_of_enrollees"),
    path('createbatch/', views.create_batch, name="create_batch")


]
