from rest_framework import serializers 
from django.contrib.auth import get_user_model
from BookHub.models import Book

class BookList(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ["id", "path", "page"]

