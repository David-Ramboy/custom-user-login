# from django.utils import timezone


from django.contrib.auth.models import AbstractUser
from django.db import models


class Custom_user(AbstractUser):
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True,blank=True, null=True)
    position = models.CharField(max_length=100,blank=True, null=True)
    company = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.email

    EMAIL_FIELD = 'email'
    ADDRESS_FIELD = 'address'
    PHONE_NUMBER_FIELD = 'phone_number'

    REQUIRED_FIELDS = ['email','address','phone_number']
    
    is_active = models.BooleanField(default=True)
   