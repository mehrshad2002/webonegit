from tkinter import Widget
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import reserve
from dashbord.models import DateMo
# from secretary.models import datesModel
class reservationForm(forms.Form):
    genders = [(1,"male"),(2,"female")]
    datesList = list(DateMo.objects.all().values_list('date',flat=True))
    date = []
    for i in datesList:
       date.append((i,i))  
    name = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class' : 'nameClass' }))
    lastName = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class' : 'lastnameClass'}))
    fatherName = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class' : 'fathernameClass'}))
    idNumber = forms.CharField(widget = forms.NumberInput(attrs = {'class' : 'idnumberClass'}))
    phoneNumber = PhoneNumberField(widget=forms.TextInput(attrs={'class' : 'phonenumberClass'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'emailClass'}))
    birthDate = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'Ex:2003-06-08', 'class' : 'birthdayClass'}))
    # reservedate = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'Ex:2003-06-08'}))
    reservedate = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class' : 'reservedateClass'}),choices=date)
    reservetime = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder':'Ex:23:59' , 'class' : 'reservetime'}))
    docName = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class' : 'reservetimeClass'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class' : 'genderClass'}),choices=genders)
