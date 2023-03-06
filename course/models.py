from django.db import models
from account.models import Custom_user

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Course(models.Model):
    category = models.ForeignKey(Category, related_name='courses',on_delete=models.CASCADE)
    course = models.CharField(max_length=255)
    duration = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.course


class Status(models.Model):
    status = models.CharField(max_length=255)
    
    def __str__(self):
        return self.status



class OrderedCourse(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'pending', 'Pending'
        PROCESSING = 'processing', 'Processing'
        PAID = 'paid', 'Paid'
        CANCELLED = 'cancelled', 'Cancelled'
        COMPLETED = 'completed', 'Completed'

    user = models.ForeignKey(Custom_user, related_name='ordered_courses',on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='ordered_courses', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    proof_of_payment = models.ImageField(upload_to='payment_images/')
    status = models.CharField(max_length=20, choices=StatusChoices.choices,default=StatusChoices.PENDING)
 
    def __str__(self):
        return self.course.course
    
class RegisterBatch(models.Model):
    user = models.ForeignKey(Custom_user,related_name='register_batch', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='register_batch', on_delete=models.CASCADE)
    batch_course_id = models.CharField(max_length=100, null=True)
    
    
    def __str__(self):
        return self.user.email
    
    class Meta:
        unique_together = [['batch_course_id']]