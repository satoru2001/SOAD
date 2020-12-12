from django.db import models


# Create your models here.

class Feedback(models.Model):
    Is_Suggestion = models.BooleanField("Suggestion", default=False)
    Is_Bug = models.BooleanField("Bug", default=False)
    Is_Question = models.BooleanField("Question", default=False)

    user_text = models.TextField(max_length=500)
    user_name = models.CharField(max_length=100)
   
    user_mail = models.EmailField()

    def __str__(self) :
        return self.user_mail
