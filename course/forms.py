from django import forms

from .models import OrderedCourse, RegisterBatch

class NewCourseForm(forms.ModelForm):
    
    class Meta:
        model = OrderedCourse
        fields = ['course','proof_of_payment']
  
class NewParticipant(forms.ModelForm):

    class Meta:
        model = RegisterBatch
        fields = ['user',] 
