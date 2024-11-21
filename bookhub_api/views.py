from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import BookList
from BookHub.models import Book

# Create your views here.


class BookList(generics.ListCreateAPIView, generics.DestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookList


   