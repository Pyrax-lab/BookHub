from django.db import models
from BookHub.models import Book
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):

    #photo_user = models.FileField(upload_to="books")
    books_read = models.ManyToManyField("BookHub.Book", blank=True, related_name = "book_related")