from django.db import models
from django.contrib.auth import get_user_model




class Book(models.Model):

    

   
    page = models.IntegerField(default=0)
    path = models.FileField(upload_to='books/', blank=True, null=True)

    


    def __str__(self):
        return str(self.path)
        

class ChekDay(models.Model):

    day = models.DateTimeField(auto_now_add=True)
    count_of_read_pages = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk)