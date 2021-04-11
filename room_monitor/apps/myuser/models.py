from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class UserProfile(AbstractUser):

    """

    用户

    """
    is_auther=models.BooleanField(default=False,verbose_name='是否认证')

    phone =models.CharField(max_length=11,verbose_name='电话')

    email = models.CharField(max_length=100,null=True,blank=True,verbose_name='邮箱')

    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        db_table = 'users.UserProfile'

        verbose_name='用户'

        verbose_name_plural = verbose_name

    def __str__(self):

        return self.username


class Code(models.Model):

    """

    验证码

    """

    phone=models.CharField(max_length=11,verbose_name='手机号')

    code=models.CharField(max_length=4,verbose_name='验证码')

    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    end_time = models.DateTimeField(default=datetime.now, verbose_name='过期时间')

    class Meta:
        db_table = 'users.Code'

        verbose_name='验证码表'

        verbose_name_plural = verbose_name

    def __str__(self):

        return self.phone


class EmailVerifyRecord(models.Model):

    """

    邮箱激活码

    """

    code = models.CharField(max_length=20, verbose_name='激活码')

    email=models.EmailField(max_length=50,verbose_name='邮箱')

    send_time=models.DateTimeField(verbose_name='发送时间',default=datetime.now)

    class Meta:

        verbose_name='邮箱验证码'

        verbose_name_plural=verbose_name

    def __str__(self):

        return '{0}({1})'.format(self.code,self.email)