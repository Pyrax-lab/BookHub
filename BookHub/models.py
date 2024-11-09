from django.db import models
from django.contrib.auth import get_user_model
# import pdfplumber
# Create your models here.


class Book(models.Model):

    


    path = models.FileField(upload_to='books/', blank=True, null=True)

    # def get_pages(self):
    #     with pdfplumber.open(self.path) as pdf:
    #         pages = models.IntegerField(default=len(pdf.pages))

    def __str__(self):
        return str(self.path)
        

