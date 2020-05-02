from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Resorts(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=30)
    base = models.IntegerField()
    adult = models.IntegerField()
    child = models.IntegerField()
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=1200)
    rating = models.IntegerField()
    phone = models.CharField(max_length=20)
    picurl = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class ReservationModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    bookDate = models.DateField()
    adult = models.IntegerField()
    child = models.IntegerField()
    resortname = models.ForeignKey(Resorts, on_delete=models.CASCADE, related_name='resortname')
    total = models.IntegerField()
