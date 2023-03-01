from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from .models import OrderedCourse,Course
from customadmin.models import TrainingBatch
from django.urls import reverse
from .forms import NewCourseForm, NewParticipant

# Create your views here.
@login_required
def detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    user = request.user

    initial_values = {
        'user': user,
        'course': course
    }

    form = NewCourseForm(request.POST or None, request.FILES or None,initial=initial_values)
    
    if request.method == 'POST':
        if form.is_valid():
            ordered_course = form.save(commit=False)
            ordered_course.price = course.price
            form.save()
          
            return redirect('../course/mycourses')
    

    return render(request, 'course/detail.html', {
        'form': form,
        'course' : course,
    })

@login_required
def my_courses(request):
    ordered_courses = OrderedCourse.objects.filter(user=request.user)
    user = request.user
    return render(request, 'course/mycourses.html',{
        'ordered_courses': ordered_courses,
        'user' : user
    })

def proofpayment(request, pk):
    ordered_courses = get_object_or_404(OrderedCourse, pk=pk)

    return render(request, 'course/proofpayment.html',{
        'ordered_courses':ordered_courses
    })

def register_batch(request, pk):
    courseOne = get_object_or_404(Course, pk=pk)
    batchcourse = TrainingBatch.objects.all().filter(course=courseOne)
    user = request.user
    
    initial_values = {
        'user': user,
        'batchcourse': batchcourse
    }

    form = NewParticipant(request.POST or None,initial=initial_values)

    if request.method == 'POST':
        if form.is_valid():
            batch_course = form.save(commit=False)
            batch_course.course = batchcourse
            form.save()
          
            return redirect('../course/mycourses')
    
    return render(request,'course/registerbatch.html',{
        'form': form,
        'batchcourse' : batchcourse,
    })