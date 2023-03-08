from django import forms

from .models import OrderedCourse, RegisterBatch

class NewCourseForm(forms.ModelForm):
   
    # category = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # price = forms.DecimalField(max_length=12, decimal_places=2, widget=forms.DecimalField(attrs={'class': 'form-control'}))
    # proof_of_payment = forms.ImageField(widget=forms.ImageField(attrs={'class': 'form-control mt-4'}))
    # status = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = OrderedCourse
        fields = ['course','proof_of_payment']

  

class NewParticipant(forms.ModelForm):

    class Meta:
        model = RegisterBatch
        fields = ['user',] 
