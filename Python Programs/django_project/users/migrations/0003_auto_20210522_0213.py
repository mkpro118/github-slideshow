# Generated by Django 3.2.3 on 2021-05-21 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210522_0201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
