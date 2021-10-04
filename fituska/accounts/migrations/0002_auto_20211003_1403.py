# Generated by Django 3.2.7 on 2021-10-03 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='karma',
        ),
        migrations.AddField(
            model_name='user',
            name='subjects',
            field=models.ManyToManyField(to='subjects.Subject'),
        ),
        migrations.CreateModel(
            name='Karma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('karma', models.IntegerField(default=0, verbose_name='karma')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subjects.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]