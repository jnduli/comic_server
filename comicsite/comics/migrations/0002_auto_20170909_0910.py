# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-09 09:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comics', '0001_initial'),
        ('sketch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='sketch',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sketch.Sketch'),
        ),
        migrations.AddField(
            model_name='comic',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]