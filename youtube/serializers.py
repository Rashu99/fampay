from rest_framework import serializers
from .models import Video, APIAuthKey


class VideoSerializer(serializers.ModelSerializer):
    """
        Class for Video Model Serialization
    """
    class Meta:
        model = Video
        fields = '__all__'


class APIAuthKeySerializer(serializers.ModelSerializer):
    """
        Class for APIAuthKey Model Serialization
    """
    class Meta:
        model = APIAuthKey
        fields = '__all__'
