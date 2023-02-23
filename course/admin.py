from django.contrib import admin

# Register your models here.
from .models import Category, Course, Status, OrderedCourse


class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'category',
        'course',
        'duration',
        'price'
    ]


class OrderedCourseAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'course',
        'price',
        'proof_of_payment',
        'status'
    ]


admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Course, CourseAdmin)
admin.site.register(OrderedCourse, OrderedCourseAdmin)
