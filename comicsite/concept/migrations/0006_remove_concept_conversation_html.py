# Generated by Django 3.2 on 2021-04-17 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concept', '0005_auto_20180407_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='concept',
            name='conversation_html',
        ),
    ]