from django.contrib import admin
from.models import Team


class TeamAdmin(admin.ModelAdmin):

    list_display = ('name_of_team', 'number_of_teammates', 'overtime_number', 'number_of_points')
    list_filter = ['number_of_points']
    search_fields = ['name_of_team']

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            kwargs['fields'] = ['name_of_team', 'number_of_teammates', 'overtime_number', ]
        else:
            kwargs['fields'] = ['name_of_team', 'number_of_teammates', ]
        return super(TeamAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Team, TeamAdmin)
