# Generated by Django 2.2.6 on 2019-12-30 16:37

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('preferences', '0002_auto_20181220_0803'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamePreferences',
            fields=[
                ('preferences_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='preferences.Preferences')),
                ('game_status', models.BooleanField(default=False, verbose_name='Gra aktywna')),
                ('overtime_question_value', models.IntegerField(default=0, verbose_name='Wartość pytania dogrywkowego')),
                ('entry_fee', models.FloatField(default=5, verbose_name='Wpisowe [zł]')),
                ('extra_reward', models.CharField(default='???', max_length=150, verbose_name='Nagroda za pytanie dogrywkowe')),
                ('current_round', models.IntegerField(default=1, verbose_name='Obecna runda')),
                ('st_place_reward', models.FloatField(default=0, verbose_name='Nagroda za pierwsze miejsce [zł]')),
                ('nd_place_reward', models.FloatField(default=0, verbose_name='Nagroda za drugie miejsce [zł]')),
                ('rd_place_reward', models.FloatField(default=0, verbose_name='Nagroda za trzecie miejsce [zł]')),
            ],
            bases=('preferences.preferences',),
            managers=[
                ('singleton', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people', models.IntegerField(verbose_name='Liczba członków drużyny')),
                ('name', models.CharField(max_length=80, verbose_name='Nazwa drużyny')),
                ('overtime_answer', models.IntegerField(blank=True, null=True, verbose_name='Liczba podana w pytaniu dogrywkowym')),
            ],
        ),
        migrations.CreateModel(
            name='PointChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scoring', models.IntegerField(default=0, verbose_name='Liczba punktów (może być ujemna)')),
                ('round_number', models.IntegerField(default=0, verbose_name='Numer rundy')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='point_changes', to='game.Team', verbose_name='Drużyna')),
            ],
        ),
    ]
