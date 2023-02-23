from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model; 

from django import forms
from .models import Custom_user
from django.core.exceptions import ValidationError
# from .models import UserRegisters
# from django.contrib.auth.forms import AuthenticationForm

# class CustomLoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))


class RegistrationForm(UserCreationForm):

    class Meta:
        User = get_user_model()
        model = User
        fields = ('username', 'address','phone_number','email','password1', 'password2')
    

    def clean(self):
       email = self.cleaned_data.get('email')
       if Custom_user.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
       return self.cleaned_data
    
    def clean(self):
       username = self.cleaned_data.get('username')
       if Custom_user.objects.filter(username=username).exists():
            raise ValidationError("Username exists")
       return self.cleaned_data
       
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'phone_number', 'address']

# class RegistrationForm(forms.ModelForm):

#     class Meta:
#         model = UserRegisters
#         fields = ('username', 'email', 'password', 're_password')
    
# widgets = {
#     'username' : forms.TextInput(attrs={
#         'placeholder' : 'Enter your Username'
#     }),
#     'email' : forms.TextInput(attrs={
#         'placeholder' : 'Enter your Email'
#     }),
#     'password' : forms.TextInput(attrs={
#         'placeholder' : 'Enter your password'
#     }),
#     're_password' : forms.TextInput(attrs={
#         'placeholder' : 'Enter your Email'
#     })
# }

    
    # username = forms.CharField(label='Username', max_length=30)
    # email = forms.EmailField(label='Email')
    # password = forms.CharField(label='Password', widget=forms.PasswordInput)