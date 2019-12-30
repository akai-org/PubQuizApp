from django.db import models
from preferences.models import Preferences


class Team(models.Model):
    people = models.IntegerField('Liczba członków drużyny')
    name = models.CharField('Nazwa drużyny', max_length=80)
    overtime_number = models.IntegerField('Liczba podana w pytaniu dogrywkowym', blank=True, null=True)

    def __str__(self):
        return self.name


class GamePreferences(Preferences):
    game_status = models.BooleanField(default=False, verbose_name="Gra aktywna")
    overtime_question_value = models.IntegerField(default=0, verbose_name="Wartość pytania dogrywkowego")
    entry_fee = models.FloatField(default=5, verbose_name="Wpisowe [zł]")
    extra_reward = models.CharField(default='???', verbose_name="Nagroda za pytanie dogrywkowe", max_length=150)
    current_round = models.IntegerField(default=1, verbose_name="Obecna runda")
    st_place_reward = models.FloatField(default=0, verbose_name="Nagroda za pierwsze miejsce [zł]")
    nd_place_reward = models.FloatField(default=0, verbose_name="Nagroda za drugie miejsce [zł]")
    rd_place_reward = models.FloatField(default=0, verbose_name="Nagroda za trzecie miejsce [zł]")


class PointChange(models.Model):
    scoring = models.IntegerField('Liczba punktów (może być ujemna)', default=0)
    round_number = models.IntegerField('Numer rundy', default=0)
    team = models.ForeignKey(Team,
                             on_delete=models.CASCADE,
                             verbose_name='Drużyna',
                             related_name='point_changes')
