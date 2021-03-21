from django.db import models
from datetime import date
# Create your models here.
import django.utils.timezone

class Sign_Recode(models.Model):
    #用来记录每天的打卡事项
    recode_chioce = (
        (1,'是'),
        (2,'否'),
    )
    id = models.AutoField('打卡记录',primary_key = True)
    sign_time = models.DateTimeField('打卡日期',default=django.utils.timezone.now)
    get_up = models.CharField('早起',choices=recode_chioce,max_length=8)
    sleep_early = models.CharField('早睡',choices=recode_chioce,max_length=8)
    english_study = models.CharField('英语学习',choices=recode_chioce,max_length=8)
    code_update = models.CharField('上传github',choices=recode_chioce,max_length=8)
    daily_recode = models.CharField('每日记录',choices=recode_chioce,max_length=8)

    class Meta:
        db_table = "sign_daily_recode"
        verbose_name = "每日打卡"
        verbose_name_plural = verbose_name


class Sign_Moon(models.Model):
    #用来记录每天的心情状况与身体状况
    moon_chioce = (
        (1,'很好'),
        (2,'较好'),
        (3,'一般'),
        (4,'较差'),
        (5,'很差'),
    )
    id = models.AutoField('身心状况',primary_key = True)
    sign_time = models.DateTimeField('打卡时间',default=django.utils.timezone.now)
    moon = models.CharField('心情状况',choices=moon_chioce,max_length=8)
    body =  models.CharField('身体状况',choices=moon_chioce,max_length=8)

    class Meta:
        db_table = "sign_daily_moon"
        verbose_name = "每日身心状况"
        verbose_name_plural = verbose_name

