from collections import UserList
from django.urls import path, include
from .views import BookList

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"books", BookList, basename="books")


urlpatterns = [

    # path("v1", BookList.as_view(), name="api_v1"),
    # path("v1/<int:pk>", BookList.as_view(), name="api_v1_pk") # для изменения данных по конкретной книге и для удаление конкретной книги

    path('', include(router.urls))

]