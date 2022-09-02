from rest_framework import serializers

from .models import Freeboard, Notice, Staffboard


class FreeboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freeboard
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'


class StaffboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffboard
        fields = '__all__'
