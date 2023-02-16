from django.contrib.auth.backends import BaseBackend

from .models import Custom_user


class EmailAuthenticationBackend(BaseBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['username'].lower()  # If you made email case insensitive add lower()
        password = kwargs['password']
        try:
            my_user = Custom_user.objects.filter(email=email).first()
        except Custom_user.DoesNotExist:
            return None
        else:
            if my_user.is_active and my_user.check_password(password):
                return my_user
        return None

    def get_user(self, user_id):
        try:
            return Custom_user.objects.filter(pk=user_id).first()
        except Custom_user.DoesNotExist:
            return None
        
# from django.contrib.auth.backends import BaseBackend
# from .models import CustomUser

# class CustomerBackend(BaseBackend):
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         try:
#             user = CustomUser.objects.get(email=email)
#         except CustomUser.DoesNotExist:
#             return None
#         if user.check_password(password):
#             return user
#         return None

#     def get_user(self, user_id):
#         try:
#             return CustomUser.objects.get(pk=user_id)
#         except CustomUser.DoesNotExist:
#             return None

