from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Book(models.Model):

    path = models.FileField(upload_to='books/', blank=True, null=True)

    def __str__(self):
        return str(self.path)
        

