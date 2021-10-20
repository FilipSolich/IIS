"""Import dummy data into DB"""

from django.contrib.auth.models import Group

from accounts.models import User, Karma
from questions.models import Question, Answer, Reaction, Rating
from subjects.models import Category, Subject, Registration

def save(lst):
    for item in lst:
        item.save()


mod = Group.objects.get(name='Moderators')

users = []

u1 = User.objects.update_or_create(login='xnovak00', email='novacek@seznam.cz', first_name='Filip', last_name='Novák', is_superuser=True)
u1.set_password('filip_novak')
users.append(u1)

u2 = User.objects.update_or_create(login='xsechr00',email='marokac@seznam.cz', first_name='Marek', last_name='Sechra')
u2.set_password('marek_sechra')
u2.groups.add(mod)
users.append(u2)

u3 = User.objects.update_or_create(login='xsolic00', email='solich@tutanota.cz', first_name='Filip', last_name='Solich')
u3.set_password('filip_solich')
u3.groups.add(mod)
users.append(u3)

u4 = User.objects.update_or_create(login='xvokal00', email='d.vokal@gmail.com', first_name='Daniel', last_name='Vokál')
u4.set_password('nejakeheslo1')
users.append(u4)

u5 = User.objects.update_or_create(login='xnamys00', email='v.myslitel@seznam.cz', first_name='Vojtěch', last_name='Namyslo')
u5.set_password('nejakeheslo2')
users.append(u5)

save(users)


subjects = []

s1 = Subject.objects.update_or_create(name='Diskretní matematika', year='2020', semester='winter', shortcut='IDM', grade=1, compulsory='compulsory',confirmed = True, user = u1)
subjects.append(s1)

s2 = Subject.objects.update_or_create(name='Diskretní matematika', year='2019', semester='winter', shortcut='IDM', grade=1,compulsory='compulsory', confirmed = True, user = u1 )
subjects.append(s2)

s3 = Subject.objects.update_or_create(name='Diskretní matematika', year='2018', semester='winter', shortcut='IDM', grade=1, compulsory='compulsory', confirmed = True, user = u2 )
subjects.append(s3)

s4 = Subject.objects.update_or_create(name='Softwarové inženýrství', year='2020', semester='winter', shortcut='IUS', grade=1, compulsory='compulsory', confirmed = True, user = u3)
subjects.append(s4)

s5 = Subject.objects.update_or_create(name='Matematická analýza 1', year ='2020', semester = 'summer', shortcut ='IMA1', grade = 1, compulsory ='compulsory', confirmed = True, user = u3 )
subjects.append(s5)

s6 = Subject.objects.update_or_create(name='Návrh číslicových systémů', year ='2020', semester = 'summer', shortcut ='INC', grade = 1, compulsory ='compulsory', confirmed = True, user = u3 )
subjects.append(s6)

s7 = Subject.objects.update_or_create(name='Algoritmy', year ='2020', semester = 'winter', shortcut ='IAL', grade = 2, compulsory ='compulsory', confirmed = True, user = u4 )
subjects.append(s7)

s8 = Subject.objects.update_or_create(name='Formální jazyky a překladače', year ='2020', semester = 'winter', shortcut ='IFJ', grade = 2, compulsory ='compulsory', confirmed = True, user = u4 )
subjects.append(s8)

s9 = Subject.objects.update_or_create(name='Kondiční posilování', year ='2020', semester = 'winter', shortcut ='TV-KP', grade = 2, compulsory ='uncompulsory', confirmed = True, user = u5 )
subjects.append(s9)

s10 = Subject.objects.update_or_create(name='Bezpečnost a počítačové sítě', year ='2020', semester = 'summer', shortcut ='IBS', grade = 2, compulsory ='uncompulsory',  confirmed = True,user = u5 )
subjects.append(s10)

save(subjects)


karma = []

k1 = Karma.objects.update_or_create(karma=10, user=u1, subject=s1)
karma.append(k1)

k2 = Karma.objects.update_or_create(karma=15, user=u1, subject=s2)
karma.append(k2)

k3 = Karma.objects.update_or_create(karma=4, user=u2, subject=s3)
karma.append(k3)

k4 = Karma.objects.update_or_create(karma=15, user=u2, subject=s4)
karma.append(k4)

k5 = Karma.objects.update_or_create(karma=20, user=u3, subject=s1)
karma.append(k5)

k6 = Karma.objects.update_or_create(karma=2, user=u3, subject=s2)
karma.append(k6)

k7 = Karma.objects.update_or_create(karma=13, user=u4, subject=s3)
karma.append(k7)

k8 = Karma.objects.update_or_create(karma=99, user=u4, subject=s4)
karma.append(k8)

save(karma)


registrations = []

r1 = Registration.objects.update_or_create(confirmed=True, user=u1, subject=s1)
registrations.append(r1)

r2 = Registration.objects.update_or_create(confirmed=True, user=u1, subject=s2)
registrations.append(r2)

r3 = Registration.objects.update_or_create(confirmed=True, user=u2, subject=s3)
registrations.append(r3)

r4 = Registration.objects.update_or_create(confirmed=True, user=u2, subject=s4)
registrations.append(r4)

r5 = Registration.objects.update_or_create(confirmed=True, user=u3, subject=s6)
registrations.append(r5)

r6 = Registration.objects.update_or_create(confirmed=True, user=u3, subject=s7)
registrations.append(r6)

r7 = Registration.objects.update_or_create(confirmed=True, user=u4, subject=s4)
registrations.append(r7)

r8 = Registration.objects.update_or_create(confirmed=True, user=u4, subject=s5)
registrations.append(r8)

r9 = Registration.objects.update_or_create(confirmed=True, user=u5, subject=s6)
registrations.append(r9)

r10 = Registration.objects.update_or_create(confirmed=False, user=u5, subject=s8)
registrations.append(r10)

r11 = Registration.objects.update_or_create(confirmed=False, user=u4, subject=s9)
registrations.append(r11)

r12 = Registration.objects.update_or_create(confirmed=False, user=u5, subject=s10)
registrations.append(r12)

save(registrations)


categories = []

c1 = Category.objects.update_or_create(name="Semestralni zkouska", subject=s1)
categories.append(c1)

c2 = Category.objects.update_or_create(name="Pulsemestralni zkouska", subject=s1)
categories.append(c2)

c3 = Category.objects.update_or_create(name="1. projekt", subject=s1)
categories.append(c3)

c4 = Category.objects.update_or_create(name="Semestralni zkouska", subject=s2)
categories.append(c4)

c5 = Category.objects.update_or_create(name="Pulsemestralni zkouska", subject=s2)
categories.append(c5)

c6 = Category.objects.update_or_create(name="Cviceni 1", subject=s2)
categories.append(c6)

c7 = Category.objects.update_or_create(name="Semestralni zkouska", subject=s3)
categories.append(c7)

c8 = Category.objects.update_or_create(name="1. projekt", subject=s4)
categories.append(c8)

c9 = Category.objects.update_or_create(name="2. projekt", subject=s4)
categories.append(c9)

c10 = Category.objects.update_or_create(name="Semestralni zkouska", subject=s5)
categories.append(c10)

c11 = Category.objects.update_or_create(name="Cviceni 1", subject=s5)
categories.append(c11)

c12 = Category.objects.update_or_create(name="Cviceni 2", subject=s5)
categories.append(c12)

c13 = Category.objects.update_or_create(name="Semestralni zkouska", subject=s6)
categories.append(c13)

c14 = Category.objects.update_or_create(name="Pulsemestralni zkouska", subject=s7)
categories.append(c14)

c15 = Category.objects.update_or_create(name="Semestralni zkouska", subject=s7)
categories.append(c15)

c16 = Category.objects.update_or_create(name="Semestralni zkouska", subject=s8)
categories.append(c16)

c17 = Category.objects.update_or_create(name="Semestralni zkouska", subject=s9)
categories.append(c17)

c18 = Category.objects.update_or_create(name="Semestralni zkouska", subject=s10)
categories.append(c18)

c19 = Category.objects.update_or_create(name="Pulsemestralni zkouska", subject=s10)
categories.append(c19)

save(categories)