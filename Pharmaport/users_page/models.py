from django.db import models
from django.contrib.auth.models import User
import datetime
import uuid

# Create your models here.
class otp(models.Model):
    passcode = models.IntegerField(null=False)
    date = models.DateTimeField(default = datetime.datetime.now)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
 
RATE_CHOICES = [
    (1,'1 - Worst Treatment'),
    (1,'2 - No results'),
    (1,'3 - OK'),
    (1,'4 - Very Good'),
    (1,'5 - Excellent'),
] 

class doc(models.Model):
    doctor_id = models.IntegerField(null=False)
    rating = models.IntegerField(null=False,default=5)
    feedback = models.TextField(null=False)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    docname = models.CharField(null=False,max_length=100,default = 'Himangshu')
    hospital = models.CharField(null=False,max_length=100,default = 'SunRise')


class connection_api(models.Model):
    connection_id =  models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    doctor_id = models.IntegerField(null=False)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.connection_id)

class files(models.Model):
    # models.URLField(max_length=200,null=False)
    name = models.CharField(max_length=20,null=False)
    metadata = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)
    uploadedfiles = models.FileField(upload_to='useruploadedfiles',null=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    via_api = models.BooleanField(default=False)
    connection = models.ForeignKey(connection_api,on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.uploadedfiles.delete()
        super().delete(*args, **kwargs)



class connections_existed(models.Model):
    doctor_id = models.IntegerField(null=False)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    date = models.DateTimeField(default = datetime.datetime.now())
