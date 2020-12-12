from django import forms


class doc(forms.Form):
    doc_id = forms.CharField(required=False,max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Doctor Id'}))
    hospital = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'placeholder': 'Hospital'}))

class data(forms.Form):
    conn_id = forms.CharField(required=True,max_length=100,widget=forms.TextInput(attrs={'placeholder': 'connection key'}))
    count = forms.IntegerField(required=False)

class dataset(forms.Form):
    name = forms.CharField(required=True,max_length=100)