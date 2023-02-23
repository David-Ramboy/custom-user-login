from django.contrib import admin

# Register your models here.
from .models import Category, Course, Status, OrderedCourse

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Status)
admin.site.register(OrderedCourse)