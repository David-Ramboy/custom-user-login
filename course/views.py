from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import OrderedCourse,Course, RegisterBatch
from customadmin.models import TrainingBatch
from .forms import NewCourseForm, NewParticipant
from django.contrib import messages
from datetime import date,datetime,time
# Create your views here.
@login_required(login_url='account:login')
def detail(request, pk1, pk2):
    course = get_object_or_404(Course, pk=pk1)
    user = request.user


    courseOne = get_object_or_404(Course, pk=pk1)
    batchcourse = TrainingBatch.objects.filter(course=courseOne) & TrainingBatch.objects.filter(id=pk2)
   
    initial_values_batch = {
        'user': user,
        'course': batchcourse
    }
    form_batch = NewParticipant(request.POST or None,initial=initial_values_batch)

    initial_values = {
        'user': user,
        'course': course
    }

    form = NewCourseForm(request.POST or None, request.FILES or None,initial=initial_values)
   
    if not RegisterBatch.objects.filter(batch_course_id=pk2).exists():
        if request.method == 'POST':
            if form.is_valid():
                batch_instance = TrainingBatch.objects.filter(course=courseOne,id=pk2)

                ordered_course = form.save(commit=False)
                ordered_course.price = course.price
                ordered_course.user = user
                form.save()
                # ----------for batch course -----------
                batch_course = form_batch.save(commit=False)
                batch_course.course = course
                batch_instance.first().participants.add(request.user)
                batch_course.batch_course_id = pk2
                form_batch.save()
            
                return redirect('course:my_courses')
    else:
        messages_text = f"A registration for this batch course already exits."
        messages.warning(request, messages_text)
    
    return render(request, 'course/enroll.html', {
        'form': form,
        'course' : course,
        'form_batch' : form_batch,
        'batchcourse' : batchcourse,

    })

@login_required(login_url='account:login')
def my_courses(request):
    ordered_courses = OrderedCourse.objects.filter(user=request.user)
    print(ordered_courses)
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

@login_required(login_url='account:login')
def register_batch(request,pk1):
    course = get_object_or_404(Course, pk=pk1)

    batchcourse = TrainingBatch.objects.filter(course=course)
    
    user = request.user

    
   
    current_date = date.today()
    current_datetime = datetime.combine(current_date, time.min)

    updated_batches = []
    for batch in batchcourse:
        batch_end_date_str = batch.end_date.strftime('%Y-%m-%d')
        batch.end_date = datetime.strptime(batch_end_date_str, '%Y-%m-%d')
        updated_batches.append(batch)
        
    for up in updated_batches:
        print(up.end_date >= current_datetime)

    return render(request,'course/registerbatch.html',{
        'user' : user,
        'batchcourse' : updated_batches,
        'course' : course,
        'current_date': current_datetime,

    })