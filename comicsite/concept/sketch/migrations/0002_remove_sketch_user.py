# Generated by Django 2.1.5 on 2019-02-06 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sketch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sketch',
            name='user',
        ),
    ]
