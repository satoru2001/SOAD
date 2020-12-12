from django import forms
from Register.models import UserProfileInfo
from django.contrib.auth.models import User
from django.core import validators

class UserForm(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput())
    verify_password=forms.CharField(widget=forms.PasswordInput())
 

    def clean(self):
        pwd=self.cleaned_data['password']
        vpwd=self.cleaned_data['verify_password']

        if pwd!=vpwd:
            raise forms.ValidationError("passwords do not match")

    class Meta():
        model = User
        fields = ('username','password','verify_password','email') 

class UserProfileInfoForm(forms.ModelForm):
    full_name=forms.CharField(max_length=264)
    phone_number=forms.CharField(max_length=10)
    Area=forms.CharField(max_length=128)
    doctor_id=forms.CharField(max_length=12)
    TRUE_FALSE_CHOICES = ( (True, 'Yes'),(False, 'No'))
    is_doctor = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, label="Are you a doctor ?", initial='', widget=forms.Select(), required=True)
    YEARS= [x for x in range(1950,2021)]
    dob= forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    class Meta():
        model = UserProfileInfo
        fields = ('full_name','phone_number','Area','dob','is_doctor','doctor_id')

