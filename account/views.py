from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .forms import RegistrationForm


def registerUser(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.save()

            return redirect('login')
    else:
        form = RegistrationForm()
    
    return render(request, 'account/register.html', {
        'form' : form,
        'title' : 'New item'
    })

def loginUser(request):
    return render(request, 'account/login.html')