# Generated by Django 3.0.5 on 2021-03-21 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0002_auto_20210321_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertoken',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 21, 21, 5, 18, 390615), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 21, 21, 5, 18, 390615), verbose_name='添加时间'),
        ),
    ]
