from collections import UserList
from django.urls import path
from .views import UsersList

urlpatterns = [

    path("v1", UserList, name="api_v1"),

]