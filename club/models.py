from django.db import models
from today.models import Product
from django.contrib.auth.models import User


class ReservationDate(models.Model):
    day_id = models.AutoField(primary_key=True)
    r_studio = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reservation_studio')
    Date = models.DateField()
    T10_11 = models.TextField(default='open')
    T11_12 = models.TextField(default='open')
    T12_13 = models.TextField(default='open')
    T13_14 = models.TextField(default='open')
    T14_15 = models.TextField(default='open')
    T15_16 = models.TextField(default='open')
    T16_17 = models.TextField(default='open')
    T17_18 = models.TextField(default='open')
    T18_19 = models.TextField(default='open')
    T19_20 = models.TextField(default='open')
    T20_21 = models.TextField(default='open')

    def __str__(self):
        return str(self.Date)


class PersonInfo(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    sur_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    mobil_phone = models.IntegerField()
    reservation_code = models.CharField(max_length=10)
    date_id = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.reservation_id}) {self.first_name} {self.sur_name}'