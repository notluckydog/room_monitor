# Generated by Django 3.1.7 on 2021-03-18 06:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0003_auto_20210315_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 18, 14, 41, 43, 873000), verbose_name='添加时间'),
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64, verbose_name='token值')),
                ('add_time', models.DateTimeField(default=datetime.datetime(2021, 3, 18, 14, 41, 43, 873000), verbose_name='添加时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myuser.myuser')),
            ],
            options={
                'verbose_name': 'token表',
                'verbose_name_plural': 'token表',
            },
        ),
    ]
