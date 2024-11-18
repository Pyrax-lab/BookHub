from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

# Create your views here.


class UsersList(generics.ListAPIView):

    queryset = get_user_model()
    serializer_class = UserSerializer()


   