from django.db import models

# Create your models here.


class Book(models.Model):

    path = models.FileField(upload_to='media/books/')

    class Meta:

        def __str__(self):
            return self.path