from django.urls import path
from .views import RegisterAPI, LoginAPI, AccountListAPI, AccountDetailAPI, MakeStaffAPI, SoftDeleteAPI

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('list/', AccountListAPI.as_view()),
    path('<str:username>/', AccountDetailAPI.as_view()),
    path('make_staff/<str:username>/', MakeStaffAPI.as_view()),
    path('delete/<str:username>/', SoftDeleteAPI.as_view()),
]
