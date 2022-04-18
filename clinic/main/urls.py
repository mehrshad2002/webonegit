from django.urls import path
from . import views
urlpatterns = [
    path('' , views.MainIndex , name = "main")
]