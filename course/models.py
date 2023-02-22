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


COLOR_CHOICES = (
    ('processing', 'Processing'),
    ('paid','Paid'),
    ('cancelled', 'Cancelled'),
    ('completed', 'Completed')
)
class Ordered_Course(models.Model):
    category = models.ForeignKey(Category, related_name='ordered_courses',on_delete=models.CASCADE)
    course = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    proof_of_payment = models.ImageField(upload_to='payment_images', blank=True, null=True)
    status = models.CharField(max_length=20, choices=COLOR_CHOICES,default='Processing')
    email = models.EmailField(unique=True,blank=True, null=True)


    def __str__(self):
        return self.course
    