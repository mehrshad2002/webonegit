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
    name = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control','id':'nameId'}))
    lastName = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','id':'lastnameId'}))
    fatherName = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control','id':'fathernameId'}))
    idNumber = forms.CharField(widget = forms.NumberInput(attrs = {'class':'form-control','id':"idNumberId"}))
    phoneNumber = PhoneNumberField(widget=forms.TextInput(attrs={'class':'form-control','id':'phoneNumberId'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','id':'emailId'}))
    birthDate = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'Ex:2003-06-08', 'class':'form-control','id':'birthDateId'}))
    # reservedate = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'Ex:2003-06-08'}))
    reserveDate = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form-control','id':'reserveDateId'}),choices=date)
    reserveTime = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder':'Ex:23:59' , 'class':'form-control','id':'reserveTimeId'}))
    docName = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','id':'docNameId'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form-control','id':'genderId'}),choices=genders)
