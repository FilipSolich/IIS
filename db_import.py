"""Import dummy data into DB"""
# README: Deprecated

from django.contrib.auth.models import Group

from accounts.models import User, Karma
from questions.models import Question, Answer, Reaction, Rating
from subjects.models import Category, Subject, Registration


mod = Group.objects.get(name='Moderators')

# User
u1 = User.objects.create(login='xnovak00', email='novacek@seznam.cz', first_name='Filip', last_name='Novák', is_superuser=True)
u1.set_password('filip_novak')
u1.save()

u2 = User.objects.create(login='xsechr00',email='marokac@seznam.cz', first_name='Marek', last_name='Sechra')
u2.set_password('marek_sechra')
u2.groups.add(mod)
u2.save()

u3 = User.objects.create(login='xsolic00', email='solich@tutanota.cz', first_name='Filip', last_name='Solich')
u3.set_password('filip_solich')
u3.groups.add(mod)
u3.save()

u4 = User.objects.create(login='xvokal00', email='d.vokal@gmail.com', first_name='Daniel', last_name='Vokál')
u4.set_password('nejakeheslo1')
u4.save()

u5 = User.objects.create(login='xnamys00', email='v.myslitel@seznam.cz', first_name='Vojtěch', last_name='Namyslo')
u5.set_password('nejakeheslo2')
u5.save()


# Subject
s1 = Subject.objects.create(name='Diskretní matematika', year='2021', semester='winter', shortcut='IDM', grade=1, compulsory='compulsory',confirmed = False, user = u1)
s2 = Subject.objects.create(name='Diskretní matematika', year='2020', semester='winter', shortcut='IDM', grade=1,compulsory='compulsory', confirmed = False, user = u1 )
s3 = Subject.objects.create(name='Diskretní matematika', year='2019', semester='winter', shortcut='IDM', grade=1, compulsory='compulsory', confirmed = False, user = u2 )
s4 = Subject.objects.create(name='Softwarové inženýrství', year='2021', semester='winter', shortcut='IUS', grade=1, compulsory='compulsory', confirmed = False, user = u3)
s5 = Subject.objects.create(name='Matematická analýza 1', year ='2021', semester = 'summer', shortcut ='IMA1', grade = 1, compulsory ='compulsory', confirmed = False, user = u3 )
s6 = Subject.objects.create(name='Návrh číslicových systémů', year ='2021', semester = 'summer', shortcut ='INC', grade = 1, compulsory ='compulsory', confirmed = True, user = u3 )
s7 = Subject.objects.create(name='Algoritmy', year ='2021', semester = 'winter', shortcut ='IAL', grade = 2, compulsory ='compulsory', confirmed = True, user = u4 )
s8 = Subject.objects.create(name='Formální jazyky a překladače', year ='2021', semester = 'winter', shortcut ='IFJ', grade = 2, compulsory ='compulsory', confirmed = True, user = u4 )
s9 = Subject.objects.create(name='Kondiční posilování', year ='2021', semester = 'winter', shortcut ='TV-KP', grade = 2, compulsory ='uncompulsory', confirmed = True, user = u5 )
s10 = Subject.objects.create(name='Bezpečnost a počítačové sítě', year ='2021', semester = 'summer', shortcut ='IBS', grade = 2, compulsory ='uncompulsory',  confirmed = True,user = u5 )

c1 = Category.objects.create(name="Semestrálni zkouška", subject=s1)
c2 = Category.objects.create(name="Půlsemestrální zkouška", subject=s1)
c3 = Category.objects.create(name="1. projekt", subject=s1)
c4 = Category.objects.create(name="Semestrálni zkouška", subject=s2)
c5 = Category.objects.create(name="Půlsemestrální zkouška", subject=s2)
c6 = Category.objects.create(name="Cvičení 1", subject=s2)
c7 = Category.objects.create(name="Semestrální zkouška", subject=s3)
c8 = Category.objects.create(name="1. projekt", subject=s4)
c9 = Category.objects.create(name="2. projekt", subject=s4)
c10 = Category.objects.create(name="Semestrálni zkouška", subject=s5)
c11 = Category.objects.create(name="Cvičení 1", subject=s5)
c12 = Category.objects.create(name="Cvičení 2", subject=s5)
c13 = Category.objects.create(name="Semestrální zkouška", subject=s6)
c14 = Category.objects.create(name="Půlsemestrální zkouška", subject=s7)
c15 = Category.objects.create(name="Semestrálni zkouška", subject=s7)
c16 = Category.objects.create(name="Semestrální zkouška", subject=s8)
c17 = Category.objects.create(name="Semestrálni zkouška", subject=s9)
c18 = Category.objects.create(name="Semestrálni zkouška", subject=s10)
c19 = Category.objects.create(name="Půlsemestrální zkouška", subject=s10)
