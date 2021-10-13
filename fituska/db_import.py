"""Import dummy data into DB"""

from accounts.models import User
from subjects.models import Subject

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


subjects = []
s1 = Subject.objects.create(name='Diskretní matematika', year ='2020', semester = 'winter', shortcut ='IDM', grade = 1, compulsory ='compulsory')
subjects.append(s1)

s2 = Subject.objects.create(name='Diskretní matematika', year ='2019', semester = 'winter', shortcut ='IDM', grade = 1,compulsory ='compulsory' )
subjects.append(s2)

s3 = Subject.objects.create(name='Diskretní matematika', year ='2018', semester = 'winter', shortcut ='IDM', grade = 1, compulsory ='compulsory' )
subjects.append(s3)

s4 = Subject.objects.create(name='Linearní algebra', year ='2020', semester = 'winter', shortcut ='ILG', grade = 1, compulsory ='compulsory' )
subjects.append(s4)

s5 = Subject.objects.create(name='Softwarové inženýrství', year ='2020', semester = 'winter', shortcut ='IUS', grade = 1, compulsory ='compulsory' )
subjects.append(s5)

s6 = Subject.objects.create(name='Základy programování', year ='2020', semester = 'winter', shortcut ='IZP', grade = 1, compulsory ='compulsory' )
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

#SAVING....

save(users)
save(subjects)



