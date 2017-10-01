# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-30 15:58
from __future__ import unicode_literals

import comicsite.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('concept', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gimp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('gimp', models.FileField(upload_to=comicsite.utils.PathAndRename('gimp'))),
                ('concept', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='concept.Concept')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
