from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, HttpResponseRedirect, get_object_or_404
from course.models import Category, Course, OrderedCourse,RegisterBatch
from .models import TrainingBatch

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
           
            form.save()
            return redirect('home')
    else:
        form = NewBatch()
        
    return render(request, 'customadmin/createbatch.html', {
        'form': form
    })

def list_of_enrollees_per_batch(request):
    course_user = RegisterBatch.objects.all()
    course_batch2 = TrainingBatch.objects.all()
    course_batch_dict = {}
    print(course_batch2)
    for batch_id in course_user:
        course_batch = TrainingBatch.objects.filter(id=batch_id.batch_course_id) 

        course_name = course_batch.first()
        if course_name not in course_batch_dict:
            course_batch_dict[course_name] = []

        for batch in course_batch:
            course_batch_dict[course_name].append(batch)
    
    print(len(course_batch_dict))

    return render(request, 'customadmin/list_of_enrollees_per_batch.html',{
         'course_batch_dict' : course_batch_dict
    })