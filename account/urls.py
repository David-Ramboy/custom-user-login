from django.urls import path
from .views import ChangePasswordView
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.login_user, name="login"),
    path('home/', views.home, name="home"),
    path('register/', views.register_user, name="register"),
    path('profile/', views.profile, name="profile"),
    path('password-change/', views.ChangePasswordView.as_view(),name="password_change"),
    path('course/', views.course, name='course'),
    path('imgpayment/<int:pk>', views.viewimgpayment, name="viewpayment"),
    path('logout/', views.user_logout, name='logout')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
