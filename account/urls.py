from django.urls import path

from . import views

urlpatterns = [
    path('', views.loginUser, name="login"),
    path('home/', views.home, name="home"),
    path('register/', views.registerUser, name="register")
]
