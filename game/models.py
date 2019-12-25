from django.db import models
from preferences.models import Preferences


class Team(models.Model):
    number_of_teammates = models.IntegerField('Liczba członków drużyny', default=0)
    number_of_points = models.IntegerField('Liczba punktów', default=0)
    name_of_team = models.CharField('Nazwa drużyny', max_length=64)
    overtime_number = models.IntegerField('Liczba podana w pytaniu dogrywkowym', blank=True, null=True, )
    
    def __str__(self):
        return self.name_of_team


class GamePreferences(Preferences):
    extra_question_value = models.IntegerField(default=0, verbose_name="Wartość pytania dogrywkowego")
    entry_fee = models.FloatField(default=5, verbose_name="Wpisowe [zł]")
    current_round = models.IntegerField(default=1, verbose_name="Obecna runda", editable=False)
    game_status = models.BooleanField(default=False, verbose_name="Gra aktywna", editable=False)
    st_place_reward = models.FloatField(default=0, verbose_name="Nagroda za pierwsze miejsce [zł]", editable=False)
    nd_place_reward = models.FloatField(default=0, verbose_name="Nagroda za drugie miejsce [zł]", editable=False)
    rd_place_reward = models.FloatField(default=0, verbose_name="Nagroda za trzecie miejsce [zł]", editable=False)
    extra_reward = models.CharField(default='???', verbose_name="Nagroda za pytanie dogrywkowe", max_length=150)
