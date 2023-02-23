from django import forms

from .models import OrderedCourse


class NewCourseForm(forms.ModelForm):
    class Meta:
        model = OrderedCourse
        fields = ('user', 'course', 'proof_of_payment')

        # widgets = {
        #     'user': forms.HiddenInput(),
        #     'course': forms.HiddenInput(),
        # }
