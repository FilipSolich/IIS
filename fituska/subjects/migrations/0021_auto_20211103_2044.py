# Generated by Django 3.2.7 on 2021-11-03 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0020_alter_subject_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='registration',
            name='confirmed',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='confirmed',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='grade',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subject',
            name='semester',
            field=models.CharField(choices=[('zimní', 'Winter'), ('letní', 'Summer')], max_length=20),
        ),
        migrations.AlterField(
            model_name='subject',
            name='shortcut',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='subject',
            name='year',
            field=models.IntegerField(),
        ),
    ]
