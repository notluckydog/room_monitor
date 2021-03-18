from django.db import models

# Create your models here.
class DeviceRun(models.Model):
    #记录传感器运行数据
    id = models.AutoField('传感器数据',primary_key = True)
    write_time = models.DateTimeField("记录时间")
    CO2_data = models.IntegerField('二氧化碳数据')
    tem_data = models.IntegerField('温度数据')
    hum_data = models.IntegerField('湿度数据')

    class Meta:
        db_table = "data_device_run"
        verbose_name = "设备运行数据"
        verbose_name_plural = verbose_name


class DeviceStatus(models.Model):
    #记录设备在线信息
    id = models.AutoField('设备在线信息',primary_key = True)
    CO2_status = models.CharField('二氧化碳传感器',default='离线',max_length=10)
    DHT11_status = models.CharField('温湿度传感器',default='离线',max_length=10)

    class Meta:
        db_table = "data_device_status"
        verbose_name = "设备在线数据"
        verbose_name_plural = verbose_name


class DeviceWarn(models.Model):
    #记录环境预警指标，例如二氧化碳最大值等
    id =models.AutoField('设备预警指标',primary_key = True)
    CO2_max = models.IntegerField('二氧化碳最大值',default='100')
    CO2_min = models.IntegerField('二氧化碳最小值',default='100')
    tem_max = models.IntegerField('温度最高值',default='85')
    tem_min = models.IntegerField('温度最低值',default='10')
    hum_max = models.IntegerField('湿度最高值',default='10')
    hum_min = models.IntegerField('湿度最小值',default='10')

    class Meta:
        db_table = "data_device_warn"
        verbose_name = "环境预警指标"
        verbose_name_plural = verbose_name

class EnvWarn(models.Model):
    #记录已产生的警告信息，例如11:00发生了温度过高
    id = models.AutoField('传感器数据', primary_key=True)
    warn_write_time = models.DateTimeField("记录时间")
    warn_CO2_data = models.IntegerField('二氧化碳数据')
    warn_tem_data = models.IntegerField('温度数据')
    warn_hum_data = models.IntegerField('湿度数据')

    class Meta:
        db_table = "data_env_warn"
        verbose_name = "环境告警信息"
        verbose_name_plural = verbose_name


