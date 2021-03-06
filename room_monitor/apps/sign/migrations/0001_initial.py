# Generated by Django 3.1.7 on 2021-04-07 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sign_Recode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='打卡记录')),
                ('sign_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='打卡日期')),
                ('get_up', models.CharField(choices=[(1, '是'), (2, '否')], max_length=8, verbose_name='早起')),
                ('sleep_early', models.CharField(choices=[(1, '是'), (2, '否')], max_length=8, verbose_name='早睡')),
                ('english_study', models.CharField(choices=[(1, '是'), (2, '否')], max_length=8, verbose_name='英语学习')),
                ('code_update', models.CharField(choices=[(1, '是'), (2, '否')], max_length=8, verbose_name='上传github')),
                ('daily_recode', models.CharField(choices=[(1, '是'), (2, '否')], max_length=8, verbose_name='每日记录')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_sign', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '每日打卡',
                'verbose_name_plural': '每日打卡',
                'db_table': 'sign_daily_recode',
            },
        ),
        migrations.CreateModel(
            name='Sign_Moon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='身心状况')),
                ('sign_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='打卡时间')),
                ('moon', models.CharField(choices=[(1, '很好'), (2, '较好'), (3, '一般'), (4, '较差'), (5, '很差')], max_length=8, verbose_name='心情状况')),
                ('body', models.CharField(choices=[(1, '很好'), (2, '较好'), (3, '一般'), (4, '较差'), (5, '很差')], max_length=8, verbose_name='身体状况')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_moon', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '每日身心状况',
                'verbose_name_plural': '每日身心状况',
                'db_table': 'sign_daily_moon',
            },
        ),
    ]
