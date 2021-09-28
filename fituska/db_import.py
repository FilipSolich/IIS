"""Import dummy data into DB"""

from accounts.models import User


def save(lst):
    for item in lst:
        item.save()


users = []

u1 = User.objects.create()
users.append(u1)

save(users)
