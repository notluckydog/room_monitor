
"""room URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from apps.myuser.views import SendCodeView,RegisterView
from apps.roomdata.views import *
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'room_data',DeviceRunView,basename='roomdata')
router.register(r'room_warn',EnvWarnView,basename='roomwarn')
router.register(r'device_status',DeviceStatusView,basename='device_status')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',include(router.urls)),
    path(r'V1/register/',RegisterView.as_view(),name ='register'),
    path(r'V1/sendcode/',SendCodeView.as_view(),name = 'sendcode'),
    path('V1/login/', obtain_jwt_token),




]
