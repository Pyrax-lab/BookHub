from collections import UserList
from django.urls import path
from .views import BookList

urlpatterns = [

    path("v1", BookList.as_view(), name="api_v1"),
    path("v1/<int:pk>", BookList.as_view(), name="api_v1_pk") # для изменения данных по конкретной книге и для удаление конкретной книги

]