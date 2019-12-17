from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    number_of_teammates = models.IntegerField('Liczba czlonkow druzyny')
    number_of_points = models.IntegerField('Liczba punktów')
    name = models.TextField('Nazwa druzyny')
    number = models.IntegerField(blank = True, null = True)

    
    def __str__(self):
        return self.name
# Create your models here.
