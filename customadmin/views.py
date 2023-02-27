from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, HttpResponseRedirect, get_object_or_404
from course.models import Category, Course, OrderedCourse

# from django.urls import HttpRes
# Create your views here.
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if username and password:

                user = authenticate(username=username, password=password)

                if user :
                    if user.is_staff:
                        if user.is_active:
                            login(request, user)
                            return redirect('./home/')
                    else:
                        messages.error(request,'You are not authorized to access this page')
                else:
                    messages.error(request,'Username or Password is Incorrect')
                
        else:
            messages.error(request, 'Fill out all the fields')

    return render(request, 'customadmin/login.html')

def home(request):
    courses = Course.objects.all()
    categories = Category.objects.all() 
    return render(request, 'customadmin/home.html',{
        'categories' : categories,
        'courses' : courses
    })


def detail(request, pk):
    course = get_object_or_404(Course, pk=pk)

    return render(request, 'customadmin/detail.html', {
        'course' : course,
    })

def list_of_enrollees(request):
    courses = Course.objects.all()
    ordered_courses = OrderedCourse.objects.all()


    return render(request, 'customadmin/list_of_enrollees.html',{
        'courses' : courses,
        'ordered_course' : ordered_courses
    })