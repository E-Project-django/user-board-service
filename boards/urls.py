from django.urls import path, include

from rest_framework import routers

from .views import FreeboardViewset, NoticeViewset, StaffboardViewset

router = routers.DefaultRouter()
router.register('freeboard', FreeboardViewset, basename='freeboard')
router.register('notice', NoticeViewset, basename='notice')
router.register('staffboard', StaffboardViewset, basename='staffboard')

urlpatterns = [
    path('', include(router.urls)),
]
