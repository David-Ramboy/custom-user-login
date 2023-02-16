from django.contrib.auth.models import User

def username_exists(username):
    return User.objects.filter(username=username).exists()