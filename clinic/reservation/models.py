from tkinter import Widget
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class reserve(models.Model):
    name = models.CharField(max_length=15)
    lastName = models.CharField(max_length=20)
    fatherName = models.TextField()
    idNumber = models.TextField()
    phoneNumber = PhoneNumberField()
    email = models.EmailField()
    birthDate = models.DateField(default="date.today")
    reservedate = models.DateField(default="date.today")
    reservetime = models.TimeField()
    docName = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
