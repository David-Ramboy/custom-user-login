from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from .models import Ordered_Course,Course
from account.models import Custom_user
from .forms import NewCourseForm

# Create your views here.
@login_required
def detail(request, pk):
    user_email = request.user.email if request.user.is_authenticated else None
    course = get_object_or_404(Course, pk=pk)
    
    if request.method == 'POST':
        form = NewCourseForm(request.POST, request.FILES, instance=course,initial={'email': user_email})

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            
            return redirect('/success/')
    else:
        form = NewCourseForm(instance=course,initial={'email': user_email})

    return render(request, 'course/detail.html', {
        'form': form,
        'course' : course,
    })
