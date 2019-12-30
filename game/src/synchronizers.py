from game.models import Team, GamePreferences
from game.src.calculations import round_down
from game.src.database import sum_value


def recalculate_rewards():
    number_of_people = sum_value(model=Team, column_name='people')
    preferences = GamePreferences.objects.first()
    if not number_of_people:
        return

    entry_fee = preferences.entry_fee
    total_money_in = entry_fee * number_of_people
    preferences.st_place_reward = round_down(total_money_in/2, 2)
    preferences.nd_place_reward = round_down(total_money_in/3, 2)
    preferences.rd_place_reward = round_down(total_money_in/6, 2)
    preferences.save()
