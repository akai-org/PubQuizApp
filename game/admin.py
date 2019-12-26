from django.contrib import admin
from preferences.admin import PreferencesAdmin
from .src import synchronizers
from .models import Team, GamePreferences


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

    def response_add(self, request, obj, post_url_continue=None):
        synchronizers.recalculate_rewards()
        return super(TeamAdmin, self).response_add(request=request, obj=obj, post_url_continue=post_url_continue)

    def response_change(self, request, obj):
        synchronizers.recalculate_rewards()
        return super(TeamAdmin, self).response_change(request=request, obj=obj)

    def response_delete(self, request, obj_display, obj_id):
        synchronizers.recalculate_rewards()
        return super(TeamAdmin, self).response_delete(request=request, obj_display=obj_display, obj_id=obj_id)


class GamePreferencesAdmin(PreferencesAdmin):
    exclude = ['sites']

    def get_readonly_fields(self, request, obj=None):
        return [
            'current_round',
            'st_place_reward',
            'nd_place_reward',
            'rd_place_reward',
        ]

    def response_add(self, request, obj, post_url_continue=None):
        synchronizers.recalculate_rewards()
        return super(GamePreferencesAdmin, self).response_add(request=request, obj=obj, post_url_continue=post_url_continue)

    def response_change(self, request, obj):
        synchronizers.recalculate_rewards()
        return super(GamePreferencesAdmin, self).response_change(request=request, obj=obj)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(Team, TeamAdmin)
admin.site.register(GamePreferences, GamePreferencesAdmin)
