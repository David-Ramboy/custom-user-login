from django import forms

from .models import TrainingBatch

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
