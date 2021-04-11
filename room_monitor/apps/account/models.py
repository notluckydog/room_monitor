import django
from django.db import models

# Create your models here.
from django.db.models import CASCADE
from ..myuser.models import UserProfile


class Expenditure(models.Model):
    #用来记录支出
    kind_type = (
        (1,'教育'),
        (2,'餐饮'),
        (3,'理财'),
        (4,'日用'),
        (5,'零食'),
        (6,'交通'),
        (7,'服饰'),
        (8,'数码'),
        (9,'住房'),
        (10,'医疗'),
    )
    id = models.AutoField('支出信息',primary_key = True)
    ex_time = models.DateTimeField('消费时间',default=django.utils.timezone.now)
    ex_kind = models.CharField('消费种类',choices=kind_type,max_length=8)
    ex_text = models.CharField('消费备注',default='无',max_length=20)
    user = models.OneToOneField(UserProfile,on_delete = models.CASCADE,
                                related_name ='user_expenditure' )

    class Meta:
        db_table = "account_expenditure"
        verbose_name = "消费支出"
        verbose_name_plural = verbose_name

class Income(models.Model):
    #收入记录
    type_income = (
        (1,'薪资'),
        (2,'退款'),
        (3,'理财'),
        (4,'兼职'),
        (5,'还钱'),
        (6,'借入'),
        (7,'意外所得'),
        (8,'报销'),
        (9,'投资'),
        (10,'其他'),
    )
    id =models.AutoField('收入信息',primary_key = True)
    in_time = models.DateTimeField('收入时间',default=django.utils.timezone.now)
    in_kind = models.CharField('收入种类',choices=type_income,max_length=8)
    in_text = models.CharField('收入备注',default='无',max_length=20)
    user = models.OneToOneField(UserProfile,on_delete = CASCADE,
                                related_name = 'user_income')

    class Meta:
        db_table = "account_income"
        verbose_name = "收入"
        verbose_name_plural = verbose_name