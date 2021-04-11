from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.sign.models import Sign_Moon, Sign_Recode
from apps.sign.serializer import Sign_Moon_Body_Serializer, Sign_Moon_Moon_Serializer, Sign_Recode_Daily_Serializer, \
    Sign_Recode_Code_Serializer, Sign_Recode_English_Serializer, Sign_Recode_Sleep_Serializer, \
    Sign_Recode_Get_up_Serializer, Sign_Moon_Serializer, Sign_Recode_Serializer


class Sign_Recode_Post(GenericViewSet):
    #用来接受用户传来的打卡信息
    # permission是用来做权限判断的
    # IsAuthenticated：必须登录用户；IsOwnerOrReadOnly：必须是当前登录的用户
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # auth使用来做用户认证的
    # authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    # s上传打卡记录
    @action(methods=['POST'], detail=False)
    def sign_recode_update(self, request):
        try:
            #获取前端传来的参数
            get_up = request.Get.get('get_up')
            sleep_early = request.Get.get('sleep_early')
            english_study = request.Get.get('english_study')
            code_update = request.Get.get('code_update')
            daily_recode = request.Get.get('daily_recode')

        except:
            return Response({'msg': '提交失败'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            #写入数据库
            sign = Sign_Recode(get_up=get_up,sleep_early=sleep_early,
                               english_study=english_study,code_update=code_update,
                               daily_recode=daily_recode)
            sign.save()

        except:
            #写入失败
            return Response({'msg': '写入失败'}, status=status.HTTP_400_BAD_REQUEST)

    # s上传身心记录
    @action(methods=['POST'], detail=False)
    def sign_moon_update(self, request):
        try:
            #获取前端传来的参数
            moon = request.Get.get('moon')
            body = request.Get.get('body')

        except:
            return Response({'msg': '提交失败'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            #写入数据库
            sign = Sign_Moon(moon=moon,body=body)
            sign.save()

        except:
            #写入失败
            return Response({'msg': '写入失败'}, status=status.HTTP_400_BAD_REQUEST)


class Data_Get(GenericViewSet):
    #用来返回数据

    #返回全部每日打卡数据
    @action(methods=['GET'], detail=False)
    def get_sign_recode_all(self, request):
        sign_time = request.Get.get('time')
        try:
            currentdata = Sign_Recode.objects.filter(sign_time=sign_time)
            serilzer = Sign_Recode_Serializer(currentdata)
            return Response(serilzer.data,status=status.HTTP_200_OK)
        except:
            return Response({'msg': '查询失败'}, status=status.HTTP_400_BAD_REQUEST)

    # 返回全部每日心情数据
    @action(methods=['GET'], detail=False)
    def get_sign_moon_all(self, request):
        sign_time = request.Get.get('time')
        try:
            currentdata = Sign_Recode.objects.filter(sign_time=sign_time)
            serilzer = Sign_Moon_Serializer(currentdata)
            return Response(serilzer.data, status=status.HTTP_200_OK)
        except:
            return Response({'msg': '查询失败'}, status=status.HTTP_400_BAD_REQUEST)

    # 返回最近一个月起床数据
    @action(methods=['GET'], detail=False)
    def get_get_up(self, request):
        #sign_time = request.Get.get('time')
        try:
            currentdata = Sign_Recode.objects.filter().order_by('-sign_time')[:30]
            serilzer = Sign_Recode_Get_up_Serializer(currentdata)
            return Response(serilzer.data, status=status.HTTP_200_OK)
        except:
            return Response({'msg': '查询失败'}, status=status.HTTP_400_BAD_REQUEST)

    # 返回最近一个月早睡数据
    @action(methods=['GET'], detail=False)
    def get_sleep(self, request):
        #sign_time = request.Get.get('time')
        try:
            currentdata = Sign_Recode.objects.filter().order_by('-sign_time')[:30]
            serilzer = Sign_Recode_Sleep_Serializer(currentdata)
            return Response(serilzer.data, status=status.HTTP_200_OK)
        except:
            return Response({'msg': '查询失败'}, status=status.HTTP_400_BAD_REQUEST)

    # 返回最近一个月英语学习数据
    @action(methods=['GET'], detail=False)
    def get_english(self, request):
        #sign_time = request.Get.get('time')
        try:
            currentdata = Sign_Recode.objects.filter().order_by('-sign_time')[:30]
            serilzer = Sign_Recode_English_Serializer(currentdata)
            return Response(serilzer.data, status=status.HTTP_200_OK)
        except:
            return Response({'msg': '查询失败'}, status=status.HTTP_400_BAD_REQUEST)

    # 返回最近一个月代码上传数据
    @action(methods=['GET'], detail=False)
    def get_code(self, request):
        #sign_time = request.Get.get('time')
        try:
            currentdata = Sign_Recode.objects.filter().order_by('-sign_time')[:30]
            serilzer = Sign_Recode_Code_Serializer(currentdata)
            return Response(serilzer.data, status=status.HTTP_200_OK)
        except:
            return Response({'msg': '查询失败'}, status=status.HTTP_400_BAD_REQUEST)

    # 返回最近一个月日记数据
    @action(methods=['GET'], detail=False)
    def get_daily_recode(self, request):
        #sign_time = request.Get.get('time')
        try:
            currentdata = Sign_Recode.objects.filter().order_by('-sign_time')[:30]
            serilzer = Sign_Recode_Daily_Serializer(currentdata)
            return Response(serilzer.data, status=status.HTTP_200_OK)
        except:
            return Response({'msg': '查询失败'}, status=status.HTTP_400_BAD_REQUEST)

    # 返回最近一个月心情数据
    @action(methods=['GET'], detail=False)
    def get_moon(self, request):
        #sign_time = request.Get.get('time')
        try:
            currentdata = Sign_Moon.objects.filter().order_by('-sign_time')[:30]
            serilzer = Sign_Moon_Moon_Serializer(currentdata)
            return Response(serilzer.data, status=status.HTTP_200_OK)
        except:
            return Response({'msg': '查询失败'}, status=status.HTTP_400_BAD_REQUEST)

    # 返回最近一个月身体数据
    @action(methods=['GET'], detail=False)
    def get_body(self, request):
        #sign_time = request.Get.get('time')
        try:
            currentdata = Sign_Moon.objects.filter().order_by('-sign_time')[:30]
            serilzer = Sign_Moon_Body_Serializer(currentdata)
            return Response(serilzer.data, status=status.HTTP_200_OK)
        except:
            return Response({'msg': '查询失败'}, status=status.HTTP_400_BAD_REQUEST)


