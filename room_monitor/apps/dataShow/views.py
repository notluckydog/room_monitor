from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action,permission_classes
# Create your views here.
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status

class DeviceRunView(GenericViewSet):
    #用来获取最新的设备数据
    # permission是用来做权限判断的
    # IsAuthenticated：必须登录用户；IsOwnerOrReadOnly：必须是当前登录的用户
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # auth使用来做用户认证的
    # authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    #查询二氧化碳浓度
    @action(methods =['GET'],detail =False)
    def get_co2(self,request):
        try:
            currntdata = DeviceRun.objects.last()
            print('good')
            print(currntdata.CO2_data)
            print(currntdata.tem_data)
            print(currntdata.hum_data)
            serlizer = CO2DeviceRunSerializer(currntdata)
            print(serlizer)
            print('happy')
            return Response(serlizer.data,status=status.HTTP_200_OK)
        except:
            return Response({'msg':'查询失败'},status=status.HTTP_400_BAD_REQUEST)



    # 查询当前温度
    @action(methods=['GET'], detail=False)
    def get_tem(self, request):
        try:
            currntdata = DeviceRun.objects.last()
            serlizer = TemDeviceRunSerializer(currntdata)
            return Response(serlizer.data, status=status.HTTP_200_OK)
        except:
            return Response({'msg': '查询失败'}, status=status.HTTP_400_BAD_REQUEST)

    # 查询湿度
    @action(methods=['GET'], detail=False)
    def get_hum(self, request):
        try:
            currntdata = DeviceRun.objects.last()
            serlizer = HumDeviceRunSerializer(currntdata)
            return Response(serlizer.data, status=status.HTTP_200_OK)
        except:
            return Response({'msg': '查询失败'}, status=status.HTTP_400_BAD_REQUEST)


class EnvWarnView(GenericViewSet):
    #用来获取环境告警信息

    # 查询告警
    @action(methods=['GET'], detail=False)
    def get_warn(self, request):
        try:
            currntdata = DeviceRun.objects.last()
            envdata = DeviceWarn.objects.last()
            if currntdata.CO2_data >= envdata.CO2_max:
                env = EnvWarn(warn_CO2_data=currntdata.CO2_data,
                              warn_tem_data=currntdata.tem_data,
                              warn_hum_data=currntdata.hum_data,
                              warn_write_time=currntdata.write_time)
                env.save()
                return Response({'msg':'CO2浓度超标，请打开窗户'},status=status.HTTP_200_OK)


            if currntdata.tem_data >= envdata.tem_max:
                env = EnvWarn(warn_CO2_data=currntdata.CO2_data,
                              warn_tem_data=currntdata.tem_data,
                              warn_hum_data=currntdata.hum_data,
                              warn_write_time=currntdata.write_time)
                env.save()
                return Response({'msg':'温度过高，请打开空调'},status=status.HTTP_200_OK)

            if currntdata.tem_data < envdata.tem_max:
                env = EnvWarn(warn_CO2_data=currntdata.CO2_data,
                              warn_tem_data=currntdata.tem_data,
                              warn_hum_data=currntdata.hum_data,
                              warn_write_time=currntdata.write_time)
                env.save()
                return Response({'msg': '温度过低，请打开暖气'}, status=status.HTTP_200_OK)

            if currntdata.hum_data >= envdata.hum_max:
                env = EnvWarn(warn_CO2_data=currntdata.CO2_data,
                              warn_tem_data=currntdata.tem_data,
                              warn_hum_data=currntdata.hum_data,
                              warn_write_time=currntdata.write_time)
                env.save()
                return Response({'msg': '湿度过高，请打开空调'}, status=status.HTTP_200_OK)

            if currntdata.hum_data >= envdata.hum_min:
                env = EnvWarn(warn_CO2_data=currntdata.CO2_data,
                              warn_tem_data=currntdata.tem_data,
                              warn_hum_data=currntdata.hum_data,
                              warn_write_time=currntdata.write_time)
                env.save()
                return Response({'msg': '温度过低，有点干燥'}, status=status.HTTP_200_OK)


        except:
            return Response({'msg': '查询失败'}, status=status.HTTP_400_BAD_REQUEST)


class DeviceStatusView(GenericViewSet):
    #用来获取设备状态
    #
    @action(methods=['GET'], detail=False)
    def get_status(self, request):
        try:
            currntdata = DeviceStatus.objects.last()
            serilzer = DeviceStatusSerialzer(currntdata)
            return Response(serilzer.data,status=status.HTTP_200_OK)
        except:
            return Response({'msg': '查询失败'}, status=status.HTTP_400_BAD_REQUEST)

