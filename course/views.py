from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.urls import reverse
from .models import Course
from account.models import Custom_user
from .forms import NewCourseForm


# Create your views here.
@login_required
def detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    user = request.user

    initial_values = {
        'user': user,
        'course': course
    }

    form = NewCourseForm(request.POST or None, request.FILES or None, initial=initial_values)

    if request.method == 'POST':
        if form.is_valid():
            ordered_course = form.save(commit=False)
            ordered_course.price = course.price
            ordered_course.save()

            return redirect(reverse('courses'))  # equivalent to /courses/

    return render(request, 'course/detail.html', {
        'form': form,
        'course': course,
    })
