"""Import dummy data into DB"""

from accounts.models import User, Karma
from questions.models import Question, Answer, Reaction, Rating
from subjects.models import Category, Subject, Registration

def save(lst):
    for item in lst:
        item.save()


mod = Group.objects.get(name='Moderators')

users = []

u1 = User.objects.create(login='xnovak00', email='novacek@seznam.cz', first_name='Filip', last_name='Novák', is_superuser=True)
u1.set_password('filip_novak')
users.append(u1)

u2 = User.objects.create(login='xsechr00',email='marokac@seznam.cz', first_name='Marek', last_name='Sechra')
u2.set_password('marek_sechra')
u2.groups.add(mod)
users.append(u2)

u3 = User.objects.create(login='xsolich00', email='solich@tutanota.cz', first_name='Filip', last_name='Solich')
u3.set_password('filip_solich')
u3.groups.add(mod)
users.append(u3)

u4 = User.objects.create(login='xvokal00', email='d.vokal@gmail.com', first_name='Daniel', last_name='Vokál')
u3.set_password('nejakeheslo1')
users.append(u4)

u5 = User.objects.create(login='xnamys00', email='v.myslitel@seznam.cz', first_name='Vojtěch', last_name='Namyslo')
u3.set_password('nejakeheslo2')
users.append(u5)

save(users)


subjects = []

s1 = Subject.objects.create(name='Diskretní matematika', year='2020', semester='winter', shortcut='IDM', grade=1, compulsory='compulsory')
subjects.append(s1)

s2 = Subject.objects.create(name='Diskretní matematika', year='2019', semester='winter', shortcut='IDM', grade=1,compulsory='compulsory' )
subjects.append(s2)

s3 = Subject.objects.create(name='Diskretní matematika', year='2018', semester='winter', shortcut='IDM', grade=1, compulsory='compulsory' )
subjects.append(s3)

s4 = Subject.objects.create(name='Linearní algebra', year='2020', semester='winter', shortcut='ILG', grade=1, compulsory='compulsory' )
subjects.append(s4)

s5 = Subject.objects.create(name='Softwarové inženýrství', year='2020', semester='winter', shortcut='IUS', grade=1, compulsory='compulsory' )
subjects.append(s5)

s6 = Subject.objects.create(name='Základy programování', year='2020', semester='winter', shortcut='IZP', grade=1, compulsory='compulsory' )
subjects.append(s6)

s7 = Subject.objects.create(name='Elektronika pro informační technologie', year ='2020', semester = 'winter', shortcut ='IEL', grade = 1, compulsory ='compulsory' )
subjects.append(s7)

s8 = Subject.objects.create(name='Matematická analýza 1', year ='2020', semester = 'summer', shortcut ='IMA1', grade = 1, compulsory ='compulsory' )
subjects.append(s8)

s9 = Subject.objects.create(name='Návrh číslicových systémů', year ='2020', semester = 'summer', shortcut ='INC', grade = 1, compulsory ='compulsory' )
subjects.append(s9)

s10 = Subject.objects.create(name='Operační systémy', year ='2020', semester = 'summer', shortcut ='IOS', grade = 1, compulsory ='compulsory' )
subjects.append(s10)

s11 = Subject.objects.create(name='Programování na strojové úrovni', year ='2020', semester = 'summer', shortcut ='ISU', grade = 1, compulsory ='compulsory' )
subjects.append(s11)

s12 = Subject.objects.create(name='Algoritmy', year ='2020', semester = 'winter', shortcut ='IAL', grade = 2, compulsory ='compulsory' )
subjects.append(s12)

s13 = Subject.objects.create(name='Formální jazyky a překladače', year ='2020', semester = 'winter', shortcut ='IFJ', grade = 2, compulsory ='compulsory' )
subjects.append(s13)

s14 = Subject.objects.create(name='Matematická analýza 2', year ='2020', semester = 'winter', shortcut ='IMA2', grade = 2, compulsory ='compulsory' )
subjects.append(s14)

s15 = Subject.objects.create(name='Návrh počítačových systémů', year ='2020', semester = 'winter', shortcut ='INP', grade = 2, compulsory ='compulsory' )
subjects.append(s15)

s16 = Subject.objects.create(name='Pravděpodobnost a statistika', year ='2020', semester = 'winter', shortcut ='IPT', grade = 2, compulsory ='compulsory' )
subjects.append(s16)

s17 = Subject.objects.create(name='Signály a systémy', year ='2020', semester = 'winter', shortcut ='IIS', grade = 2, compulsory ='compulsory' )
subjects.append(s17)

s18 = Subject.objects.create(name='Kondiční posilování', year ='2020', semester = 'winter', shortcut ='TV-KP', grade = 2, compulsory ='uncompulsory' )
subjects.append(s17)

s19 = Subject.objects.create(name='Bezpečnost a počítačové sítě', year ='2020', semester = 'summer', shortcut ='IBS', grade = 2, compulsory ='uncompulsory' )
subjects.append(s17)

save(subjects)


karma = []

k1 = Karma.objects.create(karma=10, user=u1, subject=s1)
karma.append(k1)

k2 = Karma.objects.create(karma=15, user=u1, subject=s2)
karma.append(k2)

k3 = Karma.objects.create(karma=4, user=u2, subject=s3)
karma.append(k3)

k4 = Karma.objects.create(karma=15, user=u2, subject=s4)
karma.append(k4)

k5 = Karma.objects.create(karma=20, user=u3, subject=s1)
karma.append(k5)

k6 = Karma.objects.create(karma=2, user=u3, subject=s2)
karma.append(k6)

k7 = Karma.objects.create(karma=13, user=u4, subject=s3)
karma.append(k7)

k8 = Karma.objects.create(karma=99, user=u4, subject=s4)
karma.append(k8)

save(karma)


registrations = []

r1 = Registration.objects.create(confirmed=True, user=u1, Subject=s1)
registrations.append(r1)

r2 = Registration.objects.create(confirmed=True, user=u1, Subject=s2)
registrations.append(r2)

r3 = Registration.objects.create(confirmed=True, user=u2, Subject=s3)
registrations.append(r3)

r4 = Registration.objects.create(confirmed=True, user=u2, Subject=s4)
registrations.append(r4)

r5 = Registration.objects.create(confirmed=True, user=u3, Subject=s2)
registrations.append(r5)

r6 = Registration.objects.create(confirmed=True, user=u3, Subject=s3)
registrations.append(r6)

r7 = Registration.objects.create(confirmed=True, user=u4, Subject=s4)
registrations.append(r7)

r8 = Registration.objects.create(confirmed=True, user=u4, Subject=s5)
registrations.append(r8)

r9 = Registration.objects.create(confirmed=True, user=u5, Subject=s6)
registrations.append(r9)

r10 = Registration.objects.create(confirmed=False, user=u5, Subject=s2)
registrations.append(r10)

r11 = Registration.objects.create(confirmed=False, user=u4, Subject=s5)
registrations.append(r11)

r12 = Registration.objects.create(confirmed=False, user=u5, Subject=s5)
registrations.append(r12)

save(registrations)
