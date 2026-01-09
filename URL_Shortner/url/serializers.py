from rest_framework import serializers
from .models import UrlData

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlData
        fields = '__all__'
        read_only_fields = ['slug']