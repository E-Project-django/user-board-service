from django.urls import path, include

from rest_framework import routers

from .views import FreeboardViewset, NoticeViewset, StaffboardViewset

router = routers.DefaultRouter()
router.register('freeboard', FreeboardViewset)
router.register('notice', NoticeViewset)
router.register('staffboard', StaffboardViewset)

urlpatterns = [
    path('', include(router.urls)),
]
