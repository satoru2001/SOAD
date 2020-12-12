from django import forms
from users_page.models import files,doc,RATE_CHOICES

class feedbackForm(forms.ModelForm):
    feedback = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}),required=False)
    rating = forms.ChoiceField(choices=RATE_CHOICES,widget=forms.Select(),required=True)

    class Meta:
        model = doc
        fields = ('doctor_id','docname','hospital','feedback','rating')

class filesForm(forms.ModelForm):
    class Meta:
        model = files
        fields = ('name','metadata','uploadedfiles')

