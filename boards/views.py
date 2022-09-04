from rest_framework import viewsets

from .models import Freeboard, Notice, Staffboard
from .serializers import FreeboardSerializer, FreeboardListSerializer, NoticeSerializer, NoticeListSerializer,\
    StaffboardSerializer, StaffboardListSerializer
from core.permissions import AuthorAndStaffAllEditOrReadOnly,  AuthorAndStaffAllOnly, AuthorAndStaffAllOnlyorReadOnly


class FreeboardViewset(viewsets.ModelViewSet):

    permission_classes = [AuthorAndStaffAllEditOrReadOnly]

    queryset = Freeboard.objects.all()
    serializer_class = FreeboardSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return FreeboardListSerializer
        return FreeboardSerializer


class NoticeViewset(viewsets.ModelViewSet):

    permission_classes = [AuthorAndStaffAllOnlyorReadOnly]

    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return NoticeListSerializer
        return NoticeSerializer


class StaffboardViewset(viewsets.ModelViewSet):

    permission_classes = [AuthorAndStaffAllOnly]

    queryset = Staffboard.objects.all()
    serializer_class = StaffboardSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return StaffboardListSerializer
        return StaffboardSerializer
