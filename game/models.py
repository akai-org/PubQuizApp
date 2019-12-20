from django.db import models

class Team(models.Model):
    number_of_teammates = models.IntegerField('Liczba członków drużyny',default=0)
    number_of_points = models.IntegerField('Liczba punktów',default=0)
    name_of_team = models.CharField('Nazwa drużyny',max_length=64)
    overtime_number = models.IntegerField('Liczba podana w pytaniu dogrywkowym',blank = True, null = True,)

    
    def __str__(self):
        return self.name_of_team
# Create your models here.
