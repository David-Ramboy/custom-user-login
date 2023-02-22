from django.db import models

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
    price = models.FloatField(default=0)

    def __str__(self):
        return self.course


class Status(models.Model):
    status = models.CharField(max_length=2)
    
    def __str__(self):
        return self.status

class Ordered_Course(models.Model):
    category = models.ForeignKey(Category, related_name='ordered_courses',on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='ordered_courses',on_delete=models.CASCADE)
    price = models.ForeignKey(Course, related_name='ordered_courses_price',on_delete=models.CASCADE)
    proof_of_payment = models.ImageField(upload_to='payment_images', blank=True, null=True)
    status = models.ForeignKey(Status, related_name="ordered_courses",on_delete=models.CASCADE)

    def __str__(self):
        return self.course
    