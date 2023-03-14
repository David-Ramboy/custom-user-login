from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, HttpResponseRedirect, get_object_or_404 
from course.models import Category, Course, OrderedCourse,RegisterBatch
from .models import TrainingBatch
from .decorators import admin_required
from django.urls import reverse,reverse_lazy
from .forms import NewBatch, NewCourse, UpdateCourse, UpdateUserForm
from datetime import date,datetime,time
from account.models import Custom_user
from account.forms import RegistrationForm

from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
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

@admin_required
def home(request):
    courses = Course.objects.all()
    categories = Category.objects.all() 
    return render(request, 'customadmin/home.html',{
        'categories' : categories,
        'courses' : courses
    })

@admin_required
def detail(request, pk):
    course = get_object_or_404(Course, pk=pk)

    batchcourse = TrainingBatch.objects.filter(course=course)
    
    current_date = date.today()
    current_datetime = datetime.combine(current_date, time.min)

    updated_batches = []
    order_batches_available = []
    order_batches_expire = []

    for batch in batchcourse:
        batch_end_date_str = batch.end_date.strftime('%Y-%m-%d')
        batch.end_date = datetime.strptime(batch_end_date_str, '%Y-%m-%d')
        updated_batches.append(batch)

         
    for up in updated_batches:
        # print(up.end_date >= current_datetime)
        if(up.end_date >= current_datetime):
            order_batches_available.append(up)
        
        if(up.end_date < current_datetime):
            order_batches_expire.append(up)
        
   

    sorted_batches = order_batches_available + order_batches_expire
    print(sorted_batches)

    return render(request, 'customadmin/detail.html', {
        'course' : course,
        'batchcourse' : updated_batches,
        'current_date' : current_datetime,
        'sorted_batches' : sorted_batches

    })

@admin_required
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

@admin_required
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

@admin_required
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

@admin_required
def create_course(request):
    form = NewCourse(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
           
            form.save()
            return redirect('home')
    else:
        form = NewCourse()
    return render(request, 'customadmin/create_course.html', {
        'form' : form
    })

@admin_required
def update_course(request,pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        form = UpdateCourse(request.POST or None, instance=course)

        if form.is_valid():
            course = form.save()

            return redirect(reverse('detail', args=[pk]))
    else:
        form = UpdateCourse(instance=course)
    
    return render(request, 'customadmin/update_course.html',{
        'form': form
    })
@admin_required
def users_info(request):
    users = Custom_user.objects.all()
    return render(request, 'customadmin/users_info.html',{
        'users' : users
    })

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'customadmin/changeuserpassword.html'
    success_message = "Succesfully Changed Your Password"
    success_url = reverse_lazy('users_info')

@admin_required
def edit_user(request,pk):
    user = Custom_user.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST or None, instance=user)
        
        if form.is_valid():
            user = form.save()
            messages.info(request, f'You have successfully updated your profile.')
            return HttpResponseRedirect(reverse('customadmin:home'))
    else:
        form = UpdateUserForm(instance=user)

    return render(request, 'customadmin/edit_user.html',{
        'form':form
    })

@admin_required
def create_user(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # item = form.save(commit=False)
            # item.save()
            form.save()
            return redirect('users_info')
    else:
        form = RegistrationForm()
    
    return render(request, 'customadmin/create_user.html',{
        'form' : form,
        'title' : 'New item'
    })

@admin_required
def create_batch_in_course(request,pk):
    course = get_object_or_404(Course,pk=pk)
    print(course)
    form = NewBatch(request.POST or None, initial={'course': course})

    if request.method == 'POST':
        if form.is_valid():
            formawait = form.save(commit=False)
            formawait.course = course

            form.save()
            return redirect('home')
        
    return render(request, 'customadmin/create_batch_in_course.html',{
        'course':course,
        'form' : form
    })

@admin_required
def list_all_batch(request):

    batchcourse = TrainingBatch.objects.all()
    
    current_date = date.today()
    current_datetime = datetime.combine(current_date, time.min)

    updated_batches = []
    order_batches_available = []
    order_batches_expire = []

    for batch in batchcourse:
        batch_end_date_str = batch.end_date.strftime('%Y-%m-%d')
        batch.end_date = datetime.strptime(batch_end_date_str, '%Y-%m-%d')
        updated_batches.append(batch)

         
    for up in updated_batches:
        # print(up.end_date >= current_datetime)
        if(up.end_date >= current_datetime):
            order_batches_available.append(up)
        
        if(up.end_date < current_datetime):
            order_batches_expire.append(up)
        

    sorted_batches = order_batches_available + order_batches_expire
    print(sorted_batches)
    return render(request, 'customadmin/list_all_batch.html',{
        'sorted_batches' : sorted_batches
    })