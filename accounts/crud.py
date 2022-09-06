from . import models
from django.db.models import Q


def get_all_user():
    """
    모든 유저 데이터 취득

    Returns:
        all_user_info(data_set): 모든 유저 데이터 셋
    """
    try:
        all_user_info = models.User.objects.filter(is_active=True).all()
        return all_user_info
    except Exception as e:
        print(e)


def get_time_user(start_date, end_date):
    """
    지정된 기간에 로그인 기록이 있는 유저의 데이터 취득

    Args:
        start_date (date or str): 집계 개시일
        end_date (date or str): 집계 종료일

    Returns:
        all_user_info(data_set): 지정된 기간에 로그인 기록이 있는 유저의 데이터 셋
    """
    try:
        # 집계 시작일만 지정된 경우
        if start_date == "" and end_date != "":
            all_user_info = models.User.objects.filter(
                Q(last_login__lte=end_date) & Q(is_active=True)
            )
        # 집계 종료일만 지정된 경우
        elif start_date != "" and end_date == "":
            all_user_info = models.User.objects.filter(
                Q(last_login__gte=start_date) & Q(is_active=True)
            )
        # 집계 시작&종료일이 모두 지정된 경우
        else:
            all_user_info = models.User.objects.filter(
                Q(is_active=True)
                & Q(last_login__gte=start_date)
                & Q(last_login__lte=end_date)
            )
        return all_user_info
    except Exception as e:
        print(e)


def get_all_user_count():
    """
    모든 유저의 수

    Returns:
        all_user_count(int): 모든 유저의 수
    """
    try:
        all_user_count = models.User.objects.filter(is_active=True).count()
        return all_user_count
    except Exception as e:
        print(e)
