from django.contrib import admin

# Register your models here.
from .models import Category, Course, Status, OrderedCourse, RegisterBatch

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Status)
admin.site.register(OrderedCourse)
admin.site.register(RegisterBatch)