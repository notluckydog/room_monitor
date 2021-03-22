"""room_monitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from apps.dataShow.views import *
from apps.myuser.views import *
from apps.sign_in.views import *
from rest_framework_jwt.views import obtain_jwt_token



router = DefaultRouter()
router.register(r'datarun',DeviceRunView,basename='datarun')
router.register(r'datastatus',DeviceStatusView,basename='datastatus')
router.register(r'datawarn',EnvWarnView,basename='datawarn')
router.register(r'code',SmsCodeViewset,basename = 'code')
#router.register(r'login',AuthView,basename='login')
router.register(r'users',UserViewset,basename='register')
#router.register(r'sendcode',SendCodeView,basename='sendcode')
router.register(r'code',SmsCodeViewset,basename='code')
router.register(r'signrecode',Sign_Recode_Post,basename='signrecode')
router.register(r'signdata',Data_Get,basename='signdata')



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',include(router.urls)),
    path('login/', obtain_jwt_token),
    path('jwt-auth/',obtain_jwt_token)
]
