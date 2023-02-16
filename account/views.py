from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.contrib import messages

from .forms import RegistrationForm


def register_user(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # item = form.save(commit=False)
            # item.save()
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    
    return render(request, 'account/register.html', {
        'form' : form,
        'title' : 'New item'
    })

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username and password:

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request,'Username or Password is Incorrect')
        else:
            messages.error(request, 'Fill out all the fields')

    return render(request, 'account/login.html')

def home(request):
    return render(request, 'account/home.html')