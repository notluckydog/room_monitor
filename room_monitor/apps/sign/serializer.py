from .models import *
from rest_framework import serializers

class Sign_Recode_Serializer(serializers.ModelSerializer):
    #序列化每日打卡数据
    class Meta:
        model = Sign_Recode
        fields = '__all__'

class Sign_Moon_Serializer(serializers.ModelSerializer):
    #序列化每日身心状况数据
    class Meta:
        model = Sign_Moon
        fields = '__all__'

class Sign_Recode_Get_up_Serializer(serializers.ModelSerializer):
    #序列化起床数据
    class Meta:
        model = Sign_Recode
        fields = ["sign_time","get_up"]

class Sign_Recode_Sleep_Serializer(serializers.ModelSerializer):
    #序列化早睡数据
    class Meta:
        model = Sign_Recode
        fields = ["sign_time","sleep_early"]

class Sign_Recode_English_Serializer(serializers.ModelSerializer):
    #序列化英语数据
    class Meta:
        model = Sign_Recode
        fields = ["sign_time","english_study"]

class Sign_Recode_Code_Serializer(serializers.ModelSerializer):
    #序列化英语数据
    class Meta:
        model = Sign_Recode
        fields = ["sign_time","code_update"]

class Sign_Recode_Daily_Serializer(serializers.ModelSerializer):
    #序列化每日记录数据
    class Meta:
        model = Sign_Recode
        fields = ["sign_time","daily_recode"]

class Sign_Moon_Moon_Serializer(serializers.ModelSerializer):
    #序列化心情数据
    class Meta:
        model = Sign_Moon
        fields = ["sign_time","moon"]

class Sign_Moon_Body_Serializer(serializers.ModelSerializer):
    #序列化身体数据
    class Meta:
        model = Sign_Moon
        fields = ["sign_time","body"]