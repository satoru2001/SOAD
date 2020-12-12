from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class don_sub(models.Model):
    name = models.CharField(max_length = 264)
    user = models.OneToOneField(User,on_delete=models.PROTECT,null=True)
    amount = models.IntegerField(null=False)
    transaction_id = models.CharField(max_length = 264,null=False)
    type = models.CharField(max_length=20,null=False)
    date = models.DateTimeField(null=False)
    
    def __str__(self):
        return self.transaction_id