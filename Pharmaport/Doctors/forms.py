from django import forms
import datetime
from Doctors.models import prescription,apointment_1,Profile
#['pa_id','age_1','doc_name','comp','medicine']

time_choice = (
    ("D","Morning"),
    ("A","AfterNoon"),
    ("N","Night"),
)

class pres_form(forms.ModelForm):
    pa_id=forms.CharField(widget=forms.Textarea)
    age_1=forms.CharField(widget=forms.Textarea)
    doc_name=forms.CharField(widget=forms.Textarea)
    comp=forms.CharField(widget=forms.Textarea)
    medicine=forms.CharField(widget=forms.Textarea)
    me_ch_mrg = forms.BooleanField(required=False)
    me_ch_an = forms.BooleanField(required=False)
    me_ch_n = forms.BooleanField(required=False)
    med_co=forms.CharField(widget=forms.Textarea)
    medicine_1=forms.CharField(widget=forms.Textarea ,required=False)
    me_ch_1_mrg = forms.BooleanField(required=False)
    me_ch_1_an = forms.BooleanField(required=False)
    me_ch_1_n = forms.BooleanField(required=False)
    med_1_co=forms.CharField(widget=forms.Textarea,required=False)
    medicine_2=forms.CharField(widget=forms.Textarea,required=False)
    me_ch_2_mrg = forms.BooleanField(required=False)
    me_ch_2_an = forms.BooleanField(required=False)
    me_ch_2_n = forms.BooleanField(required=False)
    med_2_co=forms.CharField(widget=forms.Textarea,required=False)
    medicine_3=forms.CharField(widget=forms.Textarea,required=False)
    me_ch_3_mrg = forms.BooleanField(required=False)
    me_ch_3_an = forms.BooleanField(required=False)
    me_ch_3_n = forms.BooleanField(required=False)
    med_3_co=forms.CharField(widget=forms.Textarea,required=False)
    medicine_4=forms.CharField(widget=forms.Textarea,required=False)
    me_ch_4_mrg = forms.BooleanField(required=False)
    me_ch_4_an = forms.BooleanField(required=False)
    me_ch_4_n = forms.BooleanField(required=False)
    med_4_co=forms.CharField(widget=forms.Textarea,required=False)
    class Meta:
        model = prescription
        fields= ['pa_id','age_1','doc_name','comp','medicine','medicine_1','medicine_2','medicine_3','medicine_4',"me_ch_mrg","me_ch_an","me_ch_n","med_co","me_ch_1_mrg","me_ch_1_an","me_ch_1_n","med_1_co","me_ch_2_mrg","me_ch_2_an","me_ch_2_n","med_2_co","me_ch_3_mrg","me_ch_3_an","me_ch_3_n","med_3_co","me_ch_4_mrg","me_ch_4_an","me_ch_4_n","med_4_co"]

class get_pres(forms.Form):
    en_id=forms.CharField(widget=forms.Textarea)

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'
class apoi_form(forms.ModelForm):
    pat_id_1 = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = apointment_1
        fields = ['pat_id_1','date_filed','time_filed']
        widgets = {'date_filed': DateInput() ,'time_filed' :TimeInput()}

class UploadDocumentForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'

GEEKS_CHOICES =( 
    ("a", "Get prescription"), 
    ("b", "Submit prescription"),
    ("c", "Get reports"),
    ("d", "Submit reports")

) 
class io(forms.Form):
    id_temp  = forms.CharField(required=True)
    otp = forms.IntegerField(required=True)

class io_1(forms.Form):
    id_temp_1  = forms.CharField(required=True)
    cars = forms.ChoiceField(choices = GEEKS_CHOICES) 


""""
class dform(forms.ModelForm):
    date_filed = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = test
        fields = ['date_filed']
 """       




