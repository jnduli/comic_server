# Generated by Django 2.2.13 on 2021-11-10 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gimp', '0003_alter_gimp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gimp',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
