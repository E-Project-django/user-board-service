from rest_framework import viewsets

from .models import Freeboard, Notice, Staffboard
from .serializers import FreeboardSerializer, NoticeSerializer, StaffboardSerializer
from core.permissions import AuthorAndStaffAllEditOrReadOnly


class FreeboardViewset(viewsets.ModelViewSet):

    permission_classes = [AuthorAndStaffAllEditOrReadOnly]

    queryset = Freeboard.objects.all()
    serializer_class = FreeboardSerializer


class NoticeViewset(viewsets.ModelViewSet):

    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


class StaffboardViewset(viewsets.ModelViewSet):

    queryset = Staffboard.objects.all()
    serializer_class = StaffboardSerializer
