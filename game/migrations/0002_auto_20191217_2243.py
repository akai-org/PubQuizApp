# Generated by Django 2.2.6 on 2019-12-17 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='name',
        ),
        migrations.RemoveField(
            model_name='team',
            name='number',
        ),
        migrations.AddField(
            model_name='team',
            name='name_of_team',
            field=models.CharField(default='Nazwa druzyny', max_length=64),
        ),
        migrations.AddField(
            model_name='team',
            name='overtime_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Liczba podana w pytaniu dogrywkowym'),
        ),
    ]
