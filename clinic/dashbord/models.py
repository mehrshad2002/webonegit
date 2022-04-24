from django.db import models
from reservation.models import reserve
# Create your models here.
class DateMo(models.Model):
    date = models.DateField()
    count = models.DecimalField(max_digits=20,decimal_places=1)
def counter():
    latest_date = reserve.objects.latest('reservedate')
    dateList  = list(DateMo.objects.all().values_list('date',flat=True))
    for date in dateList:
        if latest_date == date:
            n = DateMo.objects.get(id=dateList.index(date)).count
            DateMo.objects.get(id=dateList.index(date)).count = n - 1
