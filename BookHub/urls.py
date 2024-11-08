
from django.urls import path
from . import views
app_name = "BookHub"

urlpatterns = [
    path('', views.main, name="BookHub")
]