from django.db import models
from account.models import Custom_user
from course.models import Course, RegisterBatch
from datetime import date
import uuid
# Create your models here.

class TrainingBatch(models.Model):

    course = models.ForeignKey(Course,related_name='training_batch',on_delete=models.CASCADE)
    participants = models.ManyToManyField(Custom_user, blank=True, null=True)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    end_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return self.course.course

    
