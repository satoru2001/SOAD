from django.db import models
from django.contrib.auth.models import User
import django
import datetime
# Create your models here.
class UserProfileInfo(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  full_name=models.CharField(max_length=264,default="NoName")
  phone_number=models.CharField(max_length=10,blank = False,default=1022102112)
  Area=models.CharField(max_length=128,null=False,default="Temp")
  dob = models.DateField(default=django.utils.timezone.now)
  doctor_id=models.CharField(max_length=12,default="Not doctor",null=True)
  is_doctor = models.BooleanField(default=False)
