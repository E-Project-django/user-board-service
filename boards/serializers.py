from rest_framework import serializers

from .models import Freeboard, Notice, Staffboard


# 자유게시판 전체목록
class FreeboardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freeboard
        exclude = ['update_time']


class FreeboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freeboard
        fields = '__all__'


# 공지사항 전체목록
class NoticeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freeboard
        exclude = ['update_time']


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'


# 운영자게시판 전체목록
class StaffboardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freeboard
        exclude = ['update_time']


class StaffboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffboard
        fields = '__all__'
