from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# from .forms import

def registerUser(request):

    return render(request, 'account/register.html')

def loginUser(request):
    return render(request, 'account/login.html')