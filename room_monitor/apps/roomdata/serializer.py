from .models import *
from rest_framework import serializers

class CO2DeviceRunSerializer(serializers.ModelSerializer):
    #序列化设备运行数据
    class Meta:
        model = DeviceRun
        fields = ["CO2_data"]

class TemDeviceRunSerializer(serializers.ModelSerializer):
    #序列化设备运行数据
    class Meta:
        model = DeviceRun
        fields = ['tem_data']

class HumDeviceRunSerializer(serializers.ModelSerializer):
    #序列化设备运行数据
    class Meta:
        model = DeviceRun
        fields = ['hum_data']


class DeviceStatusSerialzer(serializers.ModelSerializer):
     #序列化设备状态数据
    class Meta:
        model = DeviceStatus
        fields = '__all__'


class EnvWarnSerializer(serializers.ModelSerializer):
    #序列化环境报警数据
    class Meta:
        model = EnvWarn
        fields = '__all__'

