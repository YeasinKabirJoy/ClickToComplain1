# Generated by Django 3.0.3 on 2020-09-22 08:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Complain', '0003_auto_20200922_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='date',
            field=models.DateField(verbose_name=datetime.date),
        ),
        migrations.AlterField(
            model_name='complain',
            name='time',
            field=models.TimeField(verbose_name=datetime.time),
        ),
    ]
