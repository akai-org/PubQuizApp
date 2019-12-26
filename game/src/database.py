from django.db.models import Sum


def sum_value(model, column_name):
    _, result = model.objects.aggregate(Sum(column_name)).popitem()
    return result
