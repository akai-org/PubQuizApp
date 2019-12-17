from django.db import models

class Team(models.Model):
    number_of_teammates = models.IntegerField('Liczba czlonkow druzyny')
    number_of_points = models.IntegerField('Liczba punktów')
    name_of_team = models.CharField(max_length=64,default='Nazwa druzyny')
    overtime_number = models.IntegerField('Liczba podana w pytaniu dogrywkowym',blank = True, null = True,)

    
    def __str__(self):
        return self.name
# Create your models here.
