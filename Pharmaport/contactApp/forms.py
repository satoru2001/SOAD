from django import forms

from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['Is_Suggestion','Is_Bug','Is_Question','user_text','user_name','user_mail']
