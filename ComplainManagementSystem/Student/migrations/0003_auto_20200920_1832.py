# Generated by Django 3.0.3 on 2020-09-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_auto_20200920_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='user_name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
