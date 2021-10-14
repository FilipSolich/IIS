"""Project handy functions"""

def get_unique_values(queryset, key):
    queryset = queryset.order_by(key)
    if key.startswith('-'):
        key = key[1:]

    multiple_values = [getattr(obj, key) for obj in queryset]
    return list(dict.fromkeys(multiple_values))
