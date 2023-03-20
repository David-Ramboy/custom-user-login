from django import forms

from .models import TrainingBatch
from course.models import Course
from django.contrib.auth import get_user_model; 

# DATE INPUT IS FOR DATES INPUT WIDGETS
class DateInput(forms.DateInput):
    input_type = 'date'

class NewBatch(forms.ModelForm):
    start_date = forms.DateField(widget=DateInput)
    end_date = forms.DateField(widget=DateInput)

    class Meta:
        model = TrainingBatch
        fields = ['course','start_date','end_date']

   
    
    # widgets = {
    #     'category' : forms.TextInput(),
    #     'course' : forms.TextInput(),
    #     'price' : forms.TextInput(),
    #     'proof_of_payment' : forms.FileInput(),
    #     'status' : forms.TextInput(),
    #     'email' : forms.TextInput()
    # }

class NewCourse(forms.ModelForm):
    
    class Meta:
        model = Course

        fields = ['category', 'course', 'duration', 'price']

class UpdateCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['category', 'course', 'duration', 'price', 'isArchived']

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    position = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    company = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = get_user_model()
        fields = ['username', 'email','company','position', 'phone_number', 'address']

class UpdateBatch(forms.ModelForm):
    start_date = forms.DateField(widget=DateInput)
    end_date = forms.DateField(widget=DateInput)

    class Meta:
        model = TrainingBatch
        fields = ['course','start_date','end_date']