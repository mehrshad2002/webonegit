from django import forms
from phonenumber_field.formfields import PhoneNumberField
class reservationForm(forms.Form):
    genders = [(1,"male"),(2,"female")]
    name = forms.CharField(max_length=15)
    lastName = forms.CharField(max_length=20)
    fatherName = forms.CharField(max_length=15)
    idNumber = forms.CharField()
    phoneNumber = PhoneNumberField()
    email = forms.EmailField()
    birthDate = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'Ex:2003-06-08', 'class' : 'birthDateClass'}))
    reservedate = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'Ex:2003-06-08' , 'class' : 'birthDateClass'}))
    reservetime = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder':'Ex:23:59', 'class' : 'birthDateClass'}))
    docName = forms.CharField(max_length=30)
    gender = forms.ChoiceField(widget=forms.RadioSelect,choices=genders)
    
