from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from .models import OrderedCourse,Course
from customadmin.models import TrainingBatch
from django.urls import reverse
from .forms import NewCourseForm, NewParticipant
from account.models import Custom_user
# Create your views here.
@login_required
def detail(request, pk1, pk2):
    course = get_object_or_404(Course, pk=pk1)
    user = request.user


    courseOne = get_object_or_404(Course, pk=pk1)
    # batch_id_request = request.POST.get('batch_id')  
    batchcourse = TrainingBatch.objects.filter(course=courseOne) & TrainingBatch.objects.filter(id=pk2)
    # batchcourse_startdate = batchcourse.values('start_date')
    # batchcourse_enddate = batchcourse.values('end_date')
    
    # startdate_string = batchcourse_startdate[0]['start_date'].strftime('%Y-%m-%d')
    # enddate_string = batchcourse_enddate[0]['end_date'].strftime('%Y-%m-%d')
    # print(batch_id.values('start_date')[0]['start_date'])
    initial_values_batch = {
        'user': user,
        'course': batchcourse
    }
    # print(batchcourse.values('id'))
    form_batch = NewParticipant(request.POST or None,initial=initial_values_batch)

    initial_values = {
        'user': user,
        'course': course
    }

    form = NewCourseForm(request.POST or None, request.FILES or None,initial=initial_values)
    
    if request.method == 'POST':
        if form.is_valid():
            batch_instance = TrainingBatch.objects.filter(course=courseOne) & TrainingBatch.objects.filter(id=pk2)

            ordered_course = form.save(commit=False)
            ordered_course.price = course.price
            ordered_course.user = user
            form.save()

            # ----------for batch course -----------
            batch_course = form_batch.save(commit=False)
            # print(batch_id_request)
            print(batch_instance.first())
            batch_course.course = batch_instance.first()
            # batch_instance.first().participants.add(request.user)
            # print(batch_id)
            batch_course.batch_course_id = pk2
            form_batch.save()
          
            return redirect('course:my_courses')
    

    return render(request, 'course/enroll.html', {
        'form': form,
        'course' : course,
        'form_batch' : form_batch,
        'batchcourse' : batchcourse,

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

@login_required
def register_batch(request,pk1):
    course = get_object_or_404(Course, pk=pk1)

    batch_id_request = request.POST.get('batch_id')  
    batchcourse = TrainingBatch.objects.filter(course=course)
    
    user = request.user
   
    # print(batchcourse.values('id'))
    
    return render(request,'course/registerbatch.html',{
        'user' : user,
        'batchcourse' : batchcourse,
        'course' : course
    })