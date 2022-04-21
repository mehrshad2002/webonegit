from django.shortcuts import render
from .forms import reservationForm
from .models import reserve

def ReserveIndex(request):
    myForm = reservationForm()
    if request.method == 'POST':
        myForm = reservationForm(request.POST)
        if myForm.is_valid():
            reserve.objects.create(**myForm.cleaned_data)
            myForm = reservationForm()
    context = {
        'form':myForm
    }
    return render(request, 'reserve.html',context)