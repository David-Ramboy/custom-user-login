from django import forms

from .models import UserRegisters
# from django.contrib.auth.forms import AuthenticationForm

# class CustomLoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = UserRegisters
        fields = ['username', 'email', 'password', 're_password']

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your Username'}))
    email =  forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter your Email'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter your Email'}))
    re_password = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter your Email'}))
    

    
    # username = forms.CharField(label='Username', max_length=30)
    # email = forms.EmailField(label='Email')
    # password = forms.CharField(label='Password', widget=forms.PasswordInput)