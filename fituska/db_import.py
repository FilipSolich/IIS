"""Import dummy data into DB"""

from accounts.models import User


def save(lst):
    for item in lst:
        item.save()


users = []

u1 = User.objects.create(login='xnovak00',email='novacek@seznam.cz',first_name='Filip',last_name="Novák")
u1.set_password("filip_novak")
users.append(u1)

u2 = User.objects.create(login='xsechr00',email='marokac@seznam.cz',first_name='Marek',last_name="Sechra")
u2.set_password("marek_sechra")
users.append(u2)

u3 = User.objects.create(login='xsolich00',email='solich@tutanota.cz',first_name='Filip',last_name="Solich")
u3.set_password("filip_solich")
users.append(u3)

u4 = User.objects.create(login='xvokal00',email='d.vokal@gmail.com',first_name='Daniel',last_name="Vokál")
users.append(u4)

u5 = User.objects.create(login='xnamys00',email='v.myslitel@seznam.cz',first_name='Vojtěch',last_name="Namyslo")
users.append(u5)

u6 = User.objects.create(login='xbohat00',email='d.bohaty@gmail.com',first_name='Damián',last_name="Bohatý")
users.append(u6)

u7 = User.objects.create(login='xsvaty00',email='svaty42@seznam.cz',first_name='Lukáš',last_name="Svatý")
users.append(u7)

u8 = User.objects.create(login='xsvetl00',email='karol.svet@gmail.com',first_name='Karolína',last_name="Světlá")
users.append(u8)

u10 = User.objects.create(login='xnemc00',email='babicka@centrum.cz',first_name='Božena',last_name="Němcová")
users.append(u10)

u9 = User.objects.create(login='xbalk00',email='m.balek00gmail.com',first_name='Mirek',last_name="Bálek")
users.append(u9)

u11 = User.objects.create(login='xsechr01',email='d.sechra@seznam.cz',first_name='David',last_name="Sechra")
users.append(u11)

save(users)

