from django.test import TestCase
from rest_framework.test import APIClient
from accounts.models import User
from datetime import datetime


class TestViews(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = APIClient()
        pass

    def test_statistics(self):
        print("start_test_statistics")
        # 더미 데이터 생성
        User.objects.create(
            age=21,
            gender="M",
            phone_number="010-2220-3343",
            username="aa",
            last_login=datetime(2022, 9, 1, 13, 10, 10),
        )
        User.objects.create(
            age=22,
            gender="M",
            phone_number="010-2221-3343",
            username="bb",
            last_login=datetime(2022, 9, 2, 14, 10, 10),
        )
        User.objects.create(
            age=23,
            gender="M",
            phone_number="010-2222-3343",
            username="cc",
            last_login=datetime(2022, 9, 3, 15, 10, 10),
        )
        User.objects.create(
            age=31,
            gender="M",
            phone_number="010-2223-3343",
            username="dd",
            last_login=datetime(2022, 9, 4, 16, 10, 10),
        )
        User.objects.create(
            age=32,
            gender="M",
            phone_number="010-2224-3343",
            username="ee",
            last_login=datetime(2022, 9, 5, 17, 10, 10),
        )
        User.objects.create(
            age=33,
            gender="F",
            phone_number="010-2225-3343",
            username="ff",
            last_login=datetime(2022, 9, 6, 18, 10, 10),
        )
        User.objects.create(
            age=34,
            gender="F",
            phone_number="010-2226-3343",
            username="gg",
            last_login=datetime(2022, 9, 7, 18, 10, 10),
        )
        User.objects.create(
            age=41,
            gender="F",
            phone_number="010-2227-3343",
            username="hh",
            last_login=datetime(2022, 9, 8, 18, 10, 10),
        )
        User.objects.create(
            age=42,
            gender="F",
            phone_number="010-2228-3343",
            username="ii",
            last_login=datetime(2022, 9, 9, 19, 10, 10),
        )
        User.objects.create(
            age=43,
            gender="F",
            phone_number="010-2229-3343",
            username="jj",
            last_login=datetime(2022, 9, 10, 19, 10, 10),
        )

        print("create")
        client = APIClient()
        # case_1 : 정상(기간 미지정, 통계목록 1~6)
        result = client.post(
            "/accounts/statistics/",
            {"start_date": "", "end_date": "", "type_list": [1, 2, 3, 4, 5, 6]},
            format="json",
        )
        print(result.data)
        exp = {
            "result": "success",
            "period": "all",
            "gender/all_user": [
                {"gender": "female", "count": 5, "percentage": 50.0},
                {"gender": "male", "count": 5, "percentage": 50.0},
            ],
            "age/all_user": [
                {"age_category": 20, "count": 3, "percentage": 30.0},
                {"age_category": 30, "count": 4, "percentage": 40.0},
                {"age_category": 40, "count": 3, "percentage": 30.0},
            ],
            "age&gender/all_user": [
                {
                    "gender": "female",
                    "age_category": 30,
                    "count": 2,
                    "percentage": 20.0,
                },
                {
                    "gender": "female",
                    "age_category": 40,
                    "count": 3,
                    "percentage": 30.0,
                },
                {"gender": "male", "age_category": 20, "count": 3, "percentage": 30.0},
                {"gender": "male", "age_category": 30, "count": 2, "percentage": 20.0},
            ],
            "age/all_male_user": [
                {"age_category": 20, "count": 3, "percentage": 60.0},
                {"age_category": 30, "count": 2, "percentage": 40.0},
            ],
            "age/all_female_user": [
                {"age_category": 30, "count": 2, "percentage": 40.0},
                {"age_category": 40, "count": 3, "percentage": 60.0},
            ],
            "hour/all_user": [
                {"time_category": 13, "count": 1, "percentage": 10.0},
                {"time_category": 14, "count": 1, "percentage": 10.0},
                {"time_category": 15, "count": 1, "percentage": 10.0},
                {"time_category": 16, "count": 1, "percentage": 10.0},
                {"time_category": 17, "count": 1, "percentage": 10.0},
                {"time_category": 18, "count": 3, "percentage": 30.0},
                {"time_category": 19, "count": 2, "percentage": 20.0},
            ],
        }
        self.assertEqual(exp, result.data)

        # case_2 : 정상(기간 지정(2022-09-01 ~ 2022-09-07)- 2022-09-01 00:00:00 ~ 2022-09-07 00:00:00 취득, 통계목록 0~6)
        result = client.post(
            "/accounts/statistics/",
            {
                "start_date": "2022-09-01",
                "end_date": "2022-09-07",
                "type_list": [0, 1, 2, 3, 4, 5, 6],
            },
            format="json",
        )
        print(result.data)
        exp = {
            "result": "success",
            "period": "2022-09-01 - 2022-09-07",
            "active_ratio": {"count": 6, "percentage": 60.0},
            "gender/all_user": [
                {"gender": "female", "count": 1, "percentage": 16.67},
                {"gender": "male", "count": 5, "percentage": 83.33},
            ],
            "age/all_user": [
                {"age_category": 20, "count": 3, "percentage": 50.0},
                {"age_category": 30, "count": 3, "percentage": 50.0},
            ],
            "age&gender/all_user": [
                {
                    "gender": "female",
                    "age_category": 30,
                    "count": 1,
                    "percentage": 16.67,
                },
                {"gender": "male", "age_category": 20, "count": 3, "percentage": 50.0},
                {"gender": "male", "age_category": 30, "count": 2, "percentage": 33.33},
            ],
            "age/all_male_user": [
                {"age_category": 20, "count": 3, "percentage": 60.0},
                {"age_category": 30, "count": 2, "percentage": 40.0},
            ],
            "age/all_female_user": [
                {"age_category": 30, "count": 1, "percentage": 100.0}
            ],
            "hour/all_user": [
                {"time_category": 13, "count": 1, "percentage": 16.67},
                {"time_category": 14, "count": 1, "percentage": 16.67},
                {"time_category": 15, "count": 1, "percentage": 16.67},
                {"time_category": 16, "count": 1, "percentage": 16.67},
                {"time_category": 17, "count": 1, "percentage": 16.67},
                {"time_category": 18, "count": 1, "percentage": 16.67},
            ],
        }
        self.assertEqual(exp, result.data)

        # case_3 : 정상(개시일만 지정, 통계목록 0~1)
        result = client.post(
            "/accounts/statistics/",
            {"start_date": "2022-09-06", "end_date": "", "type_list": [0, 1]},
            format="json",
        )
        print(result.data)
        exp = {
            "result": "success",
            "period": "2022-09-06 - ",
            "active_ratio": {"count": 5, "percentage": 50.0},
            "gender/all_user": [{"gender": "female", "count": 5, "percentage": 100.0}],
        }
        self.assertEqual(exp, result.data)

        # case_4 : 정상(종료일만 지정, 통계목록 0~1)
        result = client.post(
            "/accounts/statistics/",
            {"start_date": "", "end_date": "2022-09-06", "type_list": [0, 1]},
            format="json",
        )
        print(result.data)
        exp = {
            "result": "success",
            "period": " - 2022-09-06",
            "active_ratio": {"count": 5, "percentage": 50.0},
            "gender/all_user": [{"gender": "male", "count": 5, "percentage": 100.0}],
        }
        self.assertEqual(exp, result.data)

        # case_5 : 날짜 지정 에러
        result = client.post(
            "/accounts/statistics/",
            {
                "start_date": "2022-09-07",
                "end_date": "2022-09-01",
                "type_list": [0, 1, 2, 3, 4, 5, 6],
            },
            format="json",
        )
        print(result.data)
        print(result.status_code)
        exp = {"Message": "please check the period."}
        self.assertEqual(exp, result.data)
        self.assertEqual(400, result.status_code)
        print("finish_test_statistics")
