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



# class CustomerUserManager(UserManager):
#     def _create_user(self,email, password, **extra_fields):
#         if not email:
#             raise ValueError("You have not provided a valid e-mail address")

#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
        
#         return user

#     def create_user(self,email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self,email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self._create_user(email, password, **extra_fields)

# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(blank=True, default='', unique=True)
#     name = models.CharField(max_length=255, blank=True, default='')

#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     data_joined = models.DateTimeField(default=timezone.now)
#     last_login = models.DateTimeField(blank=True, null=True)

#     objects = CustomerUserManager()


#     USERNAME_FIELD = 'email'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'

#     def get_full_name(self):
#         return self.name

#     def get_short_name(self):
#         return self.name or self.email.split('@')[0]

# class UserRegisters(models.Model):
#     username = models.CharField(max_length=20)
#     email  = models.CharField(max_length=20)
#     password  = models.CharField(max_length=20)
#     re_password  = models.CharField(max_length=20)

#     def __str__(self):
#         return self.username
    