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
    birthDate = forms.DateField(input_formats=['%Y/%m/%d']
    )
    gender = forms.ChoiceField(choices=genders)