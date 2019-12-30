from django.db.models import Sum, Q
from django.shortcuts import render
from .models import Team
from .src.database import sum_value


def scoreboard(request):
    sorted_teams = Team.objects.all().order_by('-total_point_sum').annotate(
        total_point_sum=Sum("point_changes__scoring"),
        first_round_sum=Sum("point_changes__scoring", filter=Q(point_changes__round_number=1)),
        second_round_sum=Sum("point_changes__scoring", filter=Q(point_changes__round_number=2)),
        third_round_sum=Sum("point_changes__scoring", filter=Q(point_changes__round_number=3))
    )

    total_people = sum_value(Team, 'people')
    context = {
        'sorted_teams': sorted_teams,
        'amount_of_people': total_people
    }

    return render(request, 'scoreboard.html', context)
