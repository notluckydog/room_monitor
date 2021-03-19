from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(DeviceRun)
admin.site.register(DeviceStatus)
admin.site.register(DeviceWarn)
admin.site.register(EnvWarn)