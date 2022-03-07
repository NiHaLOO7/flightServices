from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.

class Flight(models.Model):
    flightNumber=models.CharField(max_length=100)
    operatingAirlines=models.CharField(max_length=200)
    departureCity=models.CharField(max_length=200)
    arrivalCity=models.CharField(max_length=200)
    dateOfDeparture=models.DateField()
    estimatedTimeOfDeparture=models.TimeField()

class Passenger(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    middleName = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)

class Reservation(models.Model):
    flight = models.ForeignKey(Flight,related_name='flight',on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger,related_name='passenger',on_delete=models.CASCADE)


# Just like an after insert trigger on AUTH_USER_MODEL table in the database
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)
    
