from .models import Code
from rest_framework import serializers

class CodeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ['code']
