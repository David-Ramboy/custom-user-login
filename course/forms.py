from django import forms

from .models import Ordered_Course

class NewCourseForm(forms.ModelForm):
   
    # category = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # course = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # price = forms.DecimalField(max_length=12, decimal_places=2, widget=forms.DecimalField(attrs={'class': 'form-control'}))
    # proof_of_payment = forms.ImageField(widget=forms.ImageField( required=False)(attrs={'class': 'form-control'}))
    # status = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = Ordered_Course
        fields = ('category','course','price','proof_of_payment', 'status', 'email')

    widgets = {
        'category' : forms.TextInput(),
        'course' : forms.TextInput(),
        'price' : forms.TextInput(),
        'proof_of_payment' : forms.FileInput(),
        'status' : forms.TextInput(),
        'email' : forms.TextInput()
    }
    
        
        