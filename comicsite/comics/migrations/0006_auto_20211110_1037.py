# Generated by Django 2.2.13 on 2021-11-10 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0005_auto_20210417_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='strip',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
