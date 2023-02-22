from django import forms

from .models import Ordered_Course

class NewCourseForm(forms.ModelForm):
   
    
    class Meta:
        model = Ordered_Course
        fields = ('category','course','price','proof_of_payment', 'status', 'email')

    widgets = {
        'category' : forms.TextInput(),
        'course' : forms.FileInput(),
        'price' : forms.TextInput(),
        'proof_of_payment' : forms.TextInput(),
        'status' : forms.TextInput(),
        'email' : forms.TextInput()
    }
    
        
        