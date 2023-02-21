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

    def __str__(self):
        return self.course
