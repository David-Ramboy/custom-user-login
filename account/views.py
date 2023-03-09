from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

from .forms import RegistrationForm, UpdateUserForm
from .models import Custom_user

from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

from course.models import Category, Course, OrderedCourse

def register_user(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # item = form.save(commit=False)
            # item.save()
            form.save()
            return redirect('account:login')
    else:
        form = RegistrationForm()
    
    return render(request, 'account/register.html', {
        'form' : form,
        'title' : 'New item'
    })

def login_user(request):
    logout(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username and password:

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('./home/')
            else:
                messages.error(request,'Username or Password is Incorrect')
        else:
            messages.error(request, 'Fill out all the fields')

    return render(request, 'account/login.html')

@login_required(login_url='account:login')
def home(request):
    return render(request, 'account/home.html')

@login_required(login_url='account:login')
def course(request):
    courses = Course.objects.all()
    categories = Category.objects.all() 
        
    return render(request, 'account/course.html', {
        'categories' : categories,
        'courses' : courses
    })

@login_required(login_url='account:login')
def profile(request):
    if request.method == 'POST':
        user = request.user
        form = UpdateUserForm(request.POST or None, instance=user)
        
        if form.is_valid():
            user = form.save()
            messages.info(request, f'You have successfully updated your profile.')
            return HttpResponseRedirect(reverse('account:home'))
    else:
        form = UpdateUserForm(instance=request.user)

    return render(request, 'account/profile.html',{
        'form': form
    })

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'account/changepassword.html'
    success_message = "Succesfully Changed Your Password"
    success_url = reverse_lazy('account:profile')

@login_required(login_url='account:login')
def viewimgpayment(request, pk):
    ordered_courses = get_object_or_404(OrderedCourse, pk=pk)

    return render(request, 'account/viewimgpayment.html',{
        'ordered_courses':ordered_courses
    })

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('account:login'))