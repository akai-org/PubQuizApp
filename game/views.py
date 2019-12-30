from django.db.models import Sum, Q, F
from django.db.models.functions import Abs
from django.shortcuts import render
from .models import Team, GamePreferences


def scoreboard(request):
    correct_overtime_answer = GamePreferences.objects.first().overtime_question_value
    sorted_teams = Team.objects.all().order_by('-total_point_sum', 'difference').annotate(
        total_point_sum=Sum("point_changes__scoring"),
        first_round_sum=Sum("point_changes__scoring", filter=Q(point_changes__round_number=1)),
        second_round_sum=Sum("point_changes__scoring", filter=Q(point_changes__round_number=2)),
        third_round_sum=Sum("point_changes__scoring", filter=Q(point_changes__round_number=3)),
        difference=Abs(F('overtime_answer') - correct_overtime_answer)
    )
    overtime_winning_team = sorted_teams.order_by('difference').first()
    total_people = sorted_teams.aggregate(Sum('people'))['people__sum']
    context = {
        'sorted_teams': sorted_teams,
        'amount_of_people': total_people,
        'overtime_winning_team_pk': overtime_winning_team
    }

    return render(request, 'scoreboard.html', context)
