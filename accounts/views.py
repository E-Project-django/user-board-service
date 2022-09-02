from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from . import dataprocess
from . import crud


@api_view(["POST"])
def statistics(request):
    """
    집계 기간과 통계 항목의 리스트를 인수로 받아 해당하는 항목들을 계산하여 리턴한다.

    Args:
        request (<class 'rest_framework.request.Request'>):
        request.data:
        {
            start_date : "" or "yyyy-mm-dd"  - 집계 개시일 (""인 경우 개시일 미지정) 
            end_date : "" or "yyyy-mm-dd"  - 집계 종료일 (""인 경우 종료일 미지정)
            type_list : [0 ~ 6] - 통계 항목 리스트
                type:
                    0 : 전체 회원 중 집계 기간 내 로그인 유저 비율
                    1 : 집계 기간 내 로그인 유저의 성별 비율
                    2 : 집계 기간 내 로그인 유저의 나이대 비율
                    3 : 집계 기간 내 로그인 유저의 성별과 나이대 비율
                    4 : 집계 기간 내 로그인 남성 유저의 나이대 비율
                    5 : 집계 기간 내 로그인 여성 유저의 나이대 비율
                    6 : 집계 기간 내 로그인 유저의 매 시간 별 비율
        }
        ex)
            {"start_date":"2022-09-01","end_date":"2022-09-02", "type_list":[1,2,3,4,5,6]}

    Returns:
        result (dict) : 통계 결과
    """
    try:
        result = {"result": "success"}
        # 조회 기간 지정: 해당 기간에서 통계, 조회 기간 지정하지 않음: 전체 기간에서 통계
        request_body = request.data
        start_date = request_body["start_date"]
        end_date = request_body["end_date"]
        type_list = request_body["type_list"]
        # 시작일, 종료일 중 하나라도 값이 있는 경우
        if start_date != "" or end_date != "":
            # 시작일 값이 있는 경우 -> date형식으로 변환
            if start_date != "":
                start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            # 종료일 값이 있는 경우 -> date형식으로 변환
            if end_date != "":
                end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
            result["period"] = str(start_date) + " - " + str(end_date)
            # 해당 기간의 회원정보 취득
            users_info = crud.get_time_user(start_date, end_date)
            if 0 in type_list:
                # 전체 회원 중 해당 기간 active user 비율 계산
                all_user_count = crud.get_all_user_count()
                result["active_ratio"] = {
                    "count": len(users_info),
                    "percentage": round(100 * len(users_info) / all_user_count, 2),
                }
                # 리스트에서 해당 type 제외
                type_list.remove(type_list.index(0))
        else:
            result["period"] = "all"
            # 전 기간의 회원정보 취득
            users_info = crud.get_all_user()
        # 취득한 회원정보 & 통계 목록 체크
        if len(users_info) > 0 and len(type_list) > 0:
            # 회원정보 통계
            calc_dict = dataprocess.calc_user_data(users_info, type_list)
            result.update(calc_dict)
        return Response(result)
    except Exception as e:
        return Response({"Message": e}, status=500)
