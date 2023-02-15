from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.contrib import messages
from .models import UserRegisters

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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = UserRegisters.objects.get(username=username)
            if user.password == password:
                # request.session['user_id'] = user.id
                return redirect('home')
            else:
                messages.error(request, 'Invalid password')
        except UserRegisters.DoesNotExist:
            messages.error(request, 'Invalid username')
    return render(request, 'account/login.html')

def loginUser(request):
    return render(request, 'account/home.html')