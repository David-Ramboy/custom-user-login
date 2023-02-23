from django.urls import path
from .views import ChangePasswordView

from . import views

urlpatterns = [
    path('', views.login_user, name="login"),
    path('home/', views.home, name="home"),
    path('register/', views.register_user, name="register"),
    path('profile/', views.profile, name="profile"),
    path('password-change/', views.ChangePasswordView.as_view(),name="password_change"),
    path('courses/', views.course, name='courses')

]
