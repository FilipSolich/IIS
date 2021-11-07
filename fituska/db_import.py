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

u2 = User.objects.create(login='xsechr00',email='marokac@seznam.cz', first_name='Marek', last_name='Sechra')
u2.set_password('marek_sechra')
u2.groups.add(mod)

u3 = User.objects.create(login='xsolic00', email='solich@tutanota.cz', first_name='Filip', last_name='Solich')
u3.set_password('filip_solich')
u3.groups.add(mod)

u4 = User.objects.create(login='xvokal00', email='d.vokal@gmail.com', first_name='Daniel', last_name='Vokál')
u4.set_password('nejakeheslo1')

u5 = User.objects.create(login='xnamys00', email='v.myslitel@seznam.cz', first_name='Vojtěch', last_name='Namyslo')
u5.set_password('nejakeheslo2')


# Subject
s1 = Subject.objects.create(name='Diskretní matematika', year='2020', semester='winter', shortcut='IDM', grade=1, compulsory='compulsory',confirmed = False, user = u1)
s2 = Subject.objects.create(name='Diskretní matematika', year='2019', semester='winter', shortcut='IDM', grade=1,compulsory='compulsory', confirmed = False, user = u1 )
s3 = Subject.objects.create(name='Diskretní matematika', year='2018', semester='winter', shortcut='IDM', grade=1, compulsory='compulsory', confirmed = False, user = u2 )
s4 = Subject.objects.create(name='Softwarové inženýrství', year='2020', semester='winter', shortcut='IUS', grade=1, compulsory='compulsory', confirmed = False, user = u3)
s5 = Subject.objects.create(name='Matematická analýza 1', year ='2020', semester = 'summer', shortcut ='IMA1', grade = 1, compulsory ='compulsory', confirmed = False, user = u3 )
s6 = Subject.objects.create(name='Návrh číslicových systémů', year ='2020', semester = 'summer', shortcut ='INC', grade = 1, compulsory ='compulsory', confirmed = True, user = u3 )
s7 = Subject.objects.create(name='Algoritmy', year ='2020', semester = 'winter', shortcut ='IAL', grade = 2, compulsory ='compulsory', confirmed = True, user = u4 )
s8 = Subject.objects.create(name='Formální jazyky a překladače', year ='2020', semester = 'winter', shortcut ='IFJ', grade = 2, compulsory ='compulsory', confirmed = True, user = u4 )
s9 = Subject.objects.create(name='Kondiční posilování', year ='2020', semester = 'winter', shortcut ='TV-KP', grade = 2, compulsory ='uncompulsory', confirmed = True, user = u5 )
s10 = Subject.objects.create(name='Bezpečnost a počítačové sítě', year ='2020', semester = 'summer', shortcut ='IBS', grade = 2, compulsory ='uncompulsory',  confirmed = True,user = u5 )







k1 = Karma.objects.create(karma=10, user=u1, subject=s1)
k2 = Karma.objects.create(karma=15, user=u1, subject=s2)
k3 = Karma.objects.create(karma=4, user=u2, subject=s3)
k4 = Karma.objects.create(karma=15, user=u2, subject=s4)
k5 = Karma.objects.create(karma=20, user=u3, subject=s1)
k6 = Karma.objects.create(karma=2, user=u3, subject=s2)
k7 = Karma.objects.create(karma=13, user=u4, subject=s3)
k8 = Karma.objects.create(karma=99, user=u4, subject=s4)







r1 = Registration.objects.create(confirmed=True, user=u1, subject=s1)
r2 = Registration.objects.create(confirmed=True, user=u1, subject=s2)
r3 = Registration.objects.create(confirmed=True, user=u2, subject=s3)
r4 = Registration.objects.create(confirmed=True, user=u2, subject=s4)
r5 = Registration.objects.create(confirmed=True, user=u3, subject=s6)
r6 = Registration.objects.create(confirmed=True, user=u3, subject=s7)
r7 = Registration.objects.create(confirmed=True, user=u4, subject=s4)
r8 = Registration.objects.create(confirmed=True, user=u4, subject=s5)
r9 = Registration.objects.create(confirmed=True, user=u5, subject=s6)
r10 = Registration.objects.create(confirmed=False, user=u5, subject=s8)
r11 = Registration.objects.create(confirmed=False, user=u4, subject=s9)
r12 = Registration.objects.create(confirmed=False, user=u5, subject=s10)







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




q1 = Question.objects.create(title="Náhled zkoušky",text="Dobrý den, chci se zeptat kdy bude možnost náhlednout na zkoušku ? Díky",user= u2, subject=s1, category = c1)
q2 = Question.objects.create(title="Pruběh zkoušky",text="Dobrý den, chci se zeptat jestli bude zkouška v D105 ? Nikde jsem nenašel žadné info Díky", user= u2, subject=s1, category = c1)
q3 = Question.objects.create(title="1. uloha", text="Jake bylo reseni 1. ulohy?", subject=s2, user=u1, category=c5)
q4 = Question.objects.create(title="2. uloha", text="Jake bylo reseni 2. ulohy?", subject=s2, user=u3, category=c5)
q5 = Question.objects.create(title="Cas na vypracovani", text="Dobry den, kolik casu budeme mit na vypracovani pulsemestralni zkousky?", subject=s2, user=u5, category=c5)
q6 = Question.objects.create(title="Cas", text="Dobry den, kolik casu budeme mit na vypracovani zkousky?", subject=s3, user=u3, category=c7)
q7 = Question.objects.create(title="Cviko", text="V jake laboratori bude cviceni?", subject=s2, user=u3, category=c6)
q8 = Question.objects.create(title="Ucivo", text="Dobry den, budou urcity integraly na zkousce?", subject=s3, user=u1, category=c7)
q9 = Question.objects.create(title="Forma odevzdani", text="Dobry den, v jakem formatu mame odevzdat reseni projektu?", subject=s4, user=u3, category=c8)
q10 = Question.objects.create(title="Program", text="Dobry den, chtel jsem se zeptat, v jakem programu je nejlepsi delat diagramy?", subject=s4, user=u4, category=c8)
q11 = Question.objects.create(title="Opravny termin", text="Kdy presne bude 1. opravny termin zkousky?", subject=s5, user=u1, category=c10)
q12 = Question.objects.create(title="IDE", text="Dobry den, jake vyvojove prostredi budeme na cvicenich pouzivat?", subject=s5, user=u3, category=c11)







a1 = Answer.objects.create(text="Možnost náhledu bude 21.2.2020 v kanceláří T208", valid=True, user= u1, question=q1)
a2 = Answer.objects.create(text="Zkouška bude probíhat v D105 a D0025 od 8:00", valid=True, user= u1, question=q2)
a3 = Answer.objects.create(text="Výsledkem této ulohy byl určitý integrál, který měl hodnotu 42", valid=True, user= u1, question=q3)
a4 = Answer.objects.create(text="Výsledkem byla 0", valid=True, user= u1, question=q4)
a5 = Answer.objects.create(text="Budu se na vás těšit v 7:00 a konec bude v 9:00 tudíž máte na vypracování 120min", valid=True, user= u1, question=q5)
a6 = Answer.objects.create(text="Délka je stavena na 180min začátek bude v 11:00", valid=True, user= u1, question=q6)
a7 = Answer.objects.create(text="Laboratoře probíhájí v L208", valid=True, user= u1, question=q7)
a8 = Answer.objects.create(text="Budou zde všechny integrály, které jsme probílali během semestru", valid=True, user= u1, question=q8)
a9 = Answer.objects.create(text="Prosím odevzdejte výsledky archiv ve formátu xxlogin00.zip|.targz|.rar ", valid=True, user= u1, question=q9)
a10 = Answer.objects.create(text="Pokud používáte Visual Studio doporučuji si stáhnout knihovnu na kreslení těchto diagramů nebo můžeme využít draw.io", valid=True, user= u1, question=q10)
a11 = Answer.objects.create(text="Možnost náhledu bude 8.3.2020 v kanceláří T208", valid=True, user= u1, question=q11)
a12 = Answer.objects.create(text="Budeme výhradně využivát VIM, jestli se to dá brát jako IDE", valid=True, user= u1, question=q12)

