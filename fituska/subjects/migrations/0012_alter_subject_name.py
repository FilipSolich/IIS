# Generated by Django 3.2.7 on 2021-10-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0011_auto_20211014_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Nazev předmětu'),
        ),
    ]
