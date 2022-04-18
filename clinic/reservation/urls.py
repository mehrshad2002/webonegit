from django.urls import path
from . import views
urlpatterns = [
    path( '' , views.ReserveIndex , name = "reserve")
]