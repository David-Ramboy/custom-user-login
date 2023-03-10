from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('home/', views.home, name="home"),
    path('users-info/', views.users_info, name="users_info"),
    path('edit-user/<int:pk>', views.edit_user, name="edit_user"),
    path('create-user/', views.create_user, name="create_user"),
    path('create-batch-in-course/<int:pk>', views.create_batch_in_course, name="create_batch_in_course"),
    path('user-password-change/<int:user_id>', views.change_password,name="change_password"),
    path('home/<int:pk>', views.detail, name="detail"),
    path('home/create-course', views.create_course, name="create_course"),
    path('home/update-course/<int:pk>', views.update_course, name="update_course"),
    path('listenrollees/', views.list_of_enrollees, name="list_of_enrollees"),
    path('list-all-batch/', views.list_all_batch, name="list_all_batch"),
    path('update-batch/<int:pk>/<int:pk2>', views.update_batch, name="update_batch"),
    path('update-batch-batches/<int:pk>', views.update_batch_batches, name="update_batch_batches"),
    path('createbatch/', views.create_batch, name="create_batch"),
    path('list-enrollees-per-batch/', views.list_of_enrollees_per_batch, name="list_enrollees_per_batch"),
    path('view-enrollees/<int:pk>', views.view_enrollees, name="view_enrollees")


]
