# Generated by Django 3.0.5 on 2021-03-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceRun',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='传感器数据')),
                ('write_time', models.DateTimeField(verbose_name='记录时间')),
                ('CO2_data', models.IntegerField(verbose_name='二氧化碳数据')),
                ('tem_data', models.IntegerField(verbose_name='温度数据')),
                ('hum_data', models.IntegerField(verbose_name='湿度数据')),
            ],
            options={
                'verbose_name': '设备运行数据',
                'verbose_name_plural': '设备运行数据',
                'db_table': 'data_device_run',
            },
        ),
        migrations.CreateModel(
            name='DeviceStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='设备在线信息')),
                ('status_time', models.DateTimeField(verbose_name='在线时间')),
                ('CO2_status', models.CharField(default='离线', max_length=10, verbose_name='二氧化碳传感器')),
                ('DHT11_status', models.CharField(default='离线', max_length=10, verbose_name='温湿度传感器')),
            ],
            options={
                'verbose_name': '设备在线数据',
                'verbose_name_plural': '设备在线数据',
                'db_table': 'data_device_status',
            },
        ),
        migrations.CreateModel(
            name='DeviceWarn',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='设备预警指标')),
                ('warn_time', models.DateTimeField(verbose_name='报警时间')),
                ('CO2_max', models.IntegerField(default='100', verbose_name='二氧化碳最大值')),
                ('CO2_min', models.IntegerField(default='100', verbose_name='二氧化碳最小值')),
                ('tem_max', models.IntegerField(default='85', verbose_name='温度最高值')),
                ('tem_min', models.IntegerField(default='10', verbose_name='温度最低值')),
                ('hum_max', models.IntegerField(default='10', verbose_name='湿度最高值')),
                ('hum_min', models.IntegerField(default='10', verbose_name='湿度最小值')),
            ],
            options={
                'verbose_name': '环境预警指标',
                'verbose_name_plural': '环境预警指标',
                'db_table': 'data_device_warn',
            },
        ),
        migrations.CreateModel(
            name='EnvWarn',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='传感器数据')),
                ('warn_write_time', models.DateTimeField(verbose_name='记录时间')),
                ('warn_CO2_data', models.IntegerField(verbose_name='二氧化碳数据')),
                ('warn_tem_data', models.IntegerField(verbose_name='温度数据')),
                ('warn_hum_data', models.IntegerField(verbose_name='湿度数据')),
            ],
            options={
                'verbose_name': '环境告警信息',
                'verbose_name_plural': '环境告警信息',
                'db_table': 'data_env_warn',
            },
        ),
    ]
