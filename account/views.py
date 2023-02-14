from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password= request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request,'account/login.html')

def register(request):
    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

