from django.db import models
import datetime
from django.contrib import admin

# Create your models here.
#date=models.date(default=datetime.date.today ,blank=True, null=True)
time_choice = (
    ("D","Morning"),
    ("A","AfterNoon"),
    ("N","Night"),
)
class prescription(models.Model):
    date=models.DateTimeField(default=datetime.datetime.now())
    pa_id=models.CharField(max_length=20)
    age_1=models.CharField(max_length=5)
    doc_name=models.CharField(max_length=30)
    comp=models.CharField(max_length=200)
    medicine=models.CharField(max_length=200 )
    me_ch_mrg = models.BooleanField(null=True)
    me_ch_an = models.BooleanField(null=True)
    me_ch_n = models.BooleanField(null=True)
    med_co = models.CharField(max_length=5,null=True)
    medicine_1=models.CharField(max_length=200 , null=True)
    me_ch_1_mrg = models.BooleanField(null=True)
    me_ch_1_an = models.BooleanField(null=True)
    me_ch_1_n = models.BooleanField(null=True)
    med_1_co = models.CharField(max_length=5,default="0",null=True)
    medicine_2=models.CharField(max_length=200, null=True)
    me_ch_2_mrg = models.BooleanField(null=True)
    me_ch_2_an = models.BooleanField(null=True)
    me_ch_2_n = models.BooleanField(null=True)
    med_2_co = models.CharField(max_length=5,default="0",null=True)
    medicine_3=models.CharField(max_length=200, null=True)
    me_ch_3_mrg = models.BooleanField(null=True)
    me_ch_3_an = models.BooleanField(null=True)
    me_ch_3_n = models.BooleanField(null=True)
    med_3_co = models.CharField(max_length=5,default="0",null=True)
    medicine_4=models.CharField(max_length=200, null=True)
    me_ch_4_mrg = models.BooleanField(null=True)
    me_ch_4_an = models.BooleanField(null=True)
    me_ch_4_n = models.BooleanField(null=True)
    med_4_co = models.CharField(max_length=5,default="0",null=True)

    
    def __str__(self):
        return self.age_1

class apointment_1(models.Model):
    pat_id_1=models.CharField(max_length=20)
    date_filed=models.DateField()
    time_filed=models.TimeField()

class Profile(models.Model):
   picture = models.ImageField(upload_to='media/images/')


#conda activate myDjangoEnv

