from django.db.models import Q

from rest_framework import viewsets
from rest_framework.pagination import CursorPagination

from .models import Freeboard, Notice, Staffboard
from .serializers import FreeboardSerializer, FreeboardListSerializer, NoticeSerializer, NoticeListSerializer,\
    StaffboardSerializer, StaffboardListSerializer
from core.permissions import AuthorAndStaffAllEditOrReadOnly,  AuthorAndStaffAllOnly, AuthorAndStaffAllOnlyorReadOnly


class BoardPagination(CursorPagination):
    page_size = 3
    ordering = 'id'


class FreeboardViewset(viewsets.ModelViewSet):

    permission_classes = [AuthorAndStaffAllEditOrReadOnly]

    serializer_class = FreeboardSerializer

    pagination_class =  BoardPagination

    def get_queryset(self):
        queryset = Freeboard.objects.all()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(content__icontains=search))
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return FreeboardListSerializer
        return FreeboardSerializer


class NoticeViewset(viewsets.ModelViewSet):

    permission_classes = [AuthorAndStaffAllOnlyorReadOnly]

    serializer_class = NoticeSerializer

    pagination_class = BoardPagination

    def get_queryset(self):
        queryset = Notice.objects.all()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(content__icontains=search))
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return NoticeListSerializer
        return NoticeSerializer


class StaffboardViewset(viewsets.ModelViewSet):

    permission_classes = [AuthorAndStaffAllOnly]

    serializer_class = StaffboardSerializer

    pagination_class =  BoardPagination

    def get_queryset(self):
        queryset = Staffboard.objects.all()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(content__icontains=search))
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return StaffboardListSerializer
        return StaffboardSerializer
