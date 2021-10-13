# Generated by Django 3.2.7 on 2021-10-13 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subjects', '0007_alter_subject_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='compulsory',
            field=models.CharField(choices=[('povinný', 'Compulsory'), ('nepovinný', 'Uncompulsory')], default='nepovinný', max_length=20),
        ),
        migrations.AddField(
            model_name='subject',
            name='grade',
            field=models.IntegerField(null=True, verbose_name='Year of study'),
        ),
        migrations.AddField(
            model_name='subject',
            name='shortcut',
            field=models.CharField(choices=[('zimní', 'Winter'), ('letní', 'Summer')], max_length=6, null=True, verbose_name='Short name of subject'),
        ),
        migrations.AddField(
            model_name='subject',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Nazev předmětu'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='semester',
            field=models.CharField(max_length=20, null=True, verbose_name='Semestr(Z/L)'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='year',
            field=models.IntegerField(null=True, verbose_name='Ročník'),
        ),
    ]
