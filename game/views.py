from django.shortcuts import render
from django.http import HttpResponse
from .models import Team


def scoreboard(request):
    sorted_list = Team.objects.order_by('-number_of_points','name_of_team')
    context = {'sorted_list':sorted_list}
    return render(request,'scoreboard.html',context)
