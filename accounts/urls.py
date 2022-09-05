from django.urls import path
from .views import RegisterAPI, LoginAPI, AccountListAPI, AccountDetailAPI, MakeStaffAPI, SoftDeleteAPI

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('list/', AccountListAPI.as_view(), name='list'),
    path('<str:username>/', AccountDetailAPI.as_view(), name='detail'),
    path('make_staff/<str:username>/', MakeStaffAPI.as_view(), name='make_staff'),
    path('delete/<str:username>/', SoftDeleteAPI.as_view(), name='delete'),
]
