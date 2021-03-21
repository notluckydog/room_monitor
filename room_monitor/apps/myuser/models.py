from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.
class MyUser(AbstractUser):
    #用户信息表
    id = models.AutoField(primary_key = True)
    mobile = models.TextField(max_length = 11)
    password = models.TextField(max_length=40)
    name = models.TextField(max_length=20)


    class Meta:
        managed = True
        db_table='myuser_MyUser'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class VerifyCode(models.Model):
    #验证码

    code = models.CharField("验证码",max_length=10)
    mobile = models.CharField("电话",max_length=11)
    add_time = models.DateTimeField("添加时间",default=datetime.datetime.now())

    class Meta:
        verbose_name = "短信验证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code

class UserToken(models.Model):
    #token 表
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    token = models.CharField(max_length=64,verbose_name='token值')
    add_time = models.DateTimeField(default=datetime.datetime.now(),verbose_name='添加时间')
    class Meta:
        verbose_name='token表'
        verbose_name_plural =verbose_name
    def __str__(self):
        return self.user.username
