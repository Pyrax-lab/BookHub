from django.db import models
from django.contrib.auth import get_user_model
import pdfplumber
# Create your models here.


class Book(models.Model):

    
   
    page = models.IntegerField(default=0)
    path = models.FileField(upload_to='books/', blank=True, null=True)

    

    def __str__(self):
        return str(self.path)
        

