# Generated by Django 3.2.7 on 2021-10-28 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20211024_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='validity',
        ),
        migrations.AddField(
            model_name='answer',
            name='valid',
            field=models.BooleanField(blank=True, null=True, verbose_name='valid'),
        ),
    ]
