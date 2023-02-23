from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'course'

urlpatterns = [
    path('<int:pk>', views.detail, name="detail"),
    path('mycourses/', views.my_courses, name='my_courses' ),
    path('proofpayment/', views.proofpayment, name='proofpayment' ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
