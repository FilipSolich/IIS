"""Project handy functions"""
from datetime import datetime

def get_unique_values(queryset, key):
    queryset = queryset.order_by(key)
    if key.startswith('-'):
        key = key[1:]

    multiple_values = [getattr(obj, key) for obj in queryset]
    return list(dict.fromkeys(multiple_values))


def get_current_school_years():
    date = datetime.today()
    if 1 < date.month < 8:
        return date.year - 1

    return date.year
