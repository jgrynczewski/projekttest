from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class A(models.Model):
    ...


class Place(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    points = models.DecimalField(max_digits=2 , decimal_places=1, null=True, blank=True)
    latitude = models.DecimalField(max_digits=6, decimal_places=3)
    longitude = models.DecimalField(max_digits=6, decimal_places=3)
    added = models.DateTimeField(auto_now_add=True)


class Voyage(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    source = models.ForeignKey(Place, models.SET_NULL, null=True, related_name='as_source')
    destination = models.ForeignKey(Place, models.SET_NULL, null=True, related_name='as_destination')
