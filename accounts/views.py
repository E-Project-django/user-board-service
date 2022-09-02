from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(["POST"])
def statistics(request):
    """
    집계 기간과 통계 항목의 리스트를 인수로 받아 해당하는 항목들을 계산하여 리턴한다.

    Args:
        request (<class 'rest_framework.request.Request'>):
        request.data:
        {
            start_date : "" or "yyyy-mm-dd"  - 집계 개시일
            end_date : "" or "yyyy-mm-dd"  - 집계 종료일
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
        return Response(result)
    except Exception as e:
        return Response({"Message": e}, status=500)
