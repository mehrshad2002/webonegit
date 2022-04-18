from django.shortcuts import render


def ReserveIndex(request):
    return render(request, 'reserve/reserve.html')