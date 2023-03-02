from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, HttpResponseRedirect, get_object_or_404
from course.models import Category, Course, OrderedCourse
from .models import TrainingBatch
from django.db.models import Count

from .forms import NewBatch
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
    ordered_courses = OrderedCourse.objects.select_related('user','course').all()
    course_dict = {}
    for ordered_course in ordered_courses:
        course_name = ordered_course.course.course
        if course_name not in course_dict:
            course_dict[course_name] = []
        course_dict[course_name].append(ordered_course)

    return render(request, 'customadmin/list_of_enrollees.html',{
        'courses' : courses,
        'course_dict' : course_dict
    })

def create_batch(request):

    form = NewBatch(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # item = form.save(commit=False)
            # item.save()
            form.save()
            return redirect('home')
    else:
        form = NewBatch()
        
    return render(request, 'customadmin/createbatch.html', {
        'form': form
    })

def list_of_enrollees_per_batch(request):
    course_batch = TrainingBatch.objects.select_related('course').all()
    # print(course_batch.)
    course_batch_dict = {}
    for courses in course_batch:
        course_name = courses.course.course
        if course_name not in course_batch_dict:
            course_batch_dict[course_name] = []
        course_batch_dict[course_name].append(courses)
    

        # for batch_course in batch_courses:

    return render(request, 'customadmin/list_of_enrollees_per_batch.html',{
         'course_batch_dict' : course_batch_dict
    })