import unittest
import os
import sys

sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "accounts",
    )
)
import dataprocess
from datetime import datetime
import pandas as pd


class TestDataProcess(unittest.TestCase):
    def setUp(self):
        calc_data = [
            {
                "id": 1,
                "age": 23,
                "gender": "male",
                "age_category": 20,
                "time_category": 11,
            },
            {
                "id": 2,
                "age": 33,
                "gender": "male",
                "age_category": 30,
                "time_category": 11,
            },
            {
                "id": 3,
                "age": 43,
                "gender": "male",
                "age_category": 40,
                "time_category": 12,
            },
            {
                "id": 4,
                "age": 13,
                "gender": "male",
                "age_category": 10,
                "time_category": 15,
            },
            {
                "id": 5,
                "age": 23,
                "gender": "male",
                "age_category": 20,
                "time_category": 15,
            },
            {
                "id": 6,
                "age": 33,
                "gender": "male",
                "age_category": 30,
                "time_category": 16,
            },
            {
                "id": 7,
                "age": 43,
                "gender": "male",
                "age_category": 40,
                "time_category": 16,
            },
            {
                "id": 8,
                "age": 53,
                "gender": "female",
                "age_category": 50,
                "time_category": 17,
            },
            {
                "id": 9,
                "age": 13,
                "gender": "female",
                "age_category": 10,
                "time_category": 17,
            },
            {
                "id": 10,
                "age": 63,
                "gender": "female",
                "age_category": 60,
                "time_category": 18,
            },
        ]
        global calc_df
        calc_df = pd.DataFrame(calc_data)

    def tearDown(self):
        pass

    def test_age_categorize(self):
        age = 25
        result = dataprocess.age_categorize(age)
        self.assertEqual(result, 20)

    def test_last_login_categorize(self):
        last_login = datetime(2022, 9, 22, 10, 31, 11)
        result = dataprocess.last_login_categorize(last_login)
        self.assertEqual(result, 10)

    def test_calc_ratio(self):
        data = [{"gender": "female", "id": 7}, {"gender": "male", "id": 3}]
        test_df = pd.DataFrame(data)
        result = dataprocess.calc_ratio(test_df)
        exp = [
            {"gender": "female", "count": 7, "percentage": 70.0},
            {"gender": "male", "count": 3, "percentage": 30.0},
        ]
        self.assertEqual(result, exp)

    def test_calc_type_gender(self):
        result = dataprocess.calc_type_gender(calc_df)
        exp = {
            "gender/all_user": [
                {"gender": "female", "count": 3, "percentage": 30.0},
                {"gender": "male", "count": 7, "percentage": 70.0},
            ]
        }
        self.assertEqual(result, exp)

    def test_calc_type_age(self):
        result = dataprocess.calc_type_age(calc_df)
        exp = {
            "age/all_user": [
                {"age_category": 10, "count": 2, "percentage": 20.0},
                {"age_category": 20, "count": 2, "percentage": 20.0},
                {"age_category": 30, "count": 2, "percentage": 20.0},
                {"age_category": 40, "count": 2, "percentage": 20.0},
                {"age_category": 50, "count": 1, "percentage": 10.0},
                {"age_category": 60, "count": 1, "percentage": 10.0},
            ]
        }
        self.assertEqual(result, exp)

    def test_calc_type_gender_age(self):
        result = dataprocess.calc_type_gender_age(calc_df)
        exp = {
            "age&gender/all_user": [
                {
                    "gender": "female",
                    "age_category": 10,
                    "count": 1,
                    "percentage": 10.0,
                },
                {
                    "gender": "female",
                    "age_category": 50,
                    "count": 1,
                    "percentage": 10.0,
                },
                {
                    "gender": "female",
                    "age_category": 60,
                    "count": 1,
                    "percentage": 10.0,
                },
                {"gender": "male", "age_category": 10, "count": 1, "percentage": 10.0},
                {"gender": "male", "age_category": 20, "count": 2, "percentage": 20.0},
                {"gender": "male", "age_category": 30, "count": 2, "percentage": 20.0},
                {"gender": "male", "age_category": 40, "count": 2, "percentage": 20.0},
            ]
        }
        self.assertEqual(result, exp)

    def test_calc_type_male_age(self):
        result = dataprocess.calc_type_male_age(calc_df)
        exp = {
            "age/all_male_user": [
                {"age_category": 10, "count": 1, "percentage": 14.29},
                {"age_category": 20, "count": 2, "percentage": 28.57},
                {"age_category": 30, "count": 2, "percentage": 28.57},
                {"age_category": 40, "count": 2, "percentage": 28.57},
            ]
        }
        self.assertEqual(result, exp)

    def test_type_female_age(self):
        result = dataprocess.calc_type_female_age(calc_df)
        exp = {
            "age/all_female_user": [
                {"age_category": 10, "count": 1, "percentage": 33.33},
                {"age_category": 50, "count": 1, "percentage": 33.33},
                {"age_category": 60, "count": 1, "percentage": 33.33},
            ]
        }
        self.assertEqual(result, exp)

    def test_type_hour(self):
        result = dataprocess.calc_type_hour(calc_df)
        exp = {
            "hour/all_user": [
                {"time_category": 11, "count": 2, "percentage": 20.0},
                {"time_category": 12, "count": 1, "percentage": 10.0},
                {"time_category": 15, "count": 2, "percentage": 20.0},
                {"time_category": 16, "count": 2, "percentage": 20.0},
                {"time_category": 17, "count": 2, "percentage": 20.0},
                {"time_category": 18, "count": 1, "percentage": 10.0},
            ]
        }
        self.assertEqual(result, exp)

    def test_calc_user_data(self):
        user_data = [
            {
                "id": 1,
                "age": 23,
                "gender": "F",
                "last_login": datetime(2022, 9, 1, 10, 30, 0),
            },
            {
                "id": 2,
                "age": 33,
                "gender": "F",
                "last_login": datetime(2022, 9, 1, 11, 30, 0),
            },
            {
                "id": 3,
                "age": 43,
                "gender": "F",
                "last_login": datetime(2022, 9, 1, 12, 30, 0),
            },
            {
                "id": 4,
                "age": 13,
                "gender": "F",
                "last_login": datetime(2022, 9, 1, 13, 30, 0),
            },
            {
                "id": 8,
                "age": 53,
                "gender": "F",
                "last_login": datetime(2022, 9, 1, 14, 30, 0),
            },
            {
                "id": 5,
                "age": 23,
                "gender": "M",
                "last_login": datetime(2022, 9, 1, 15, 30, 0),
            },
            {
                "id": 6,
                "age": 33,
                "gender": "M",
                "last_login": datetime(2022, 9, 1, 16, 30, 0),
            },
            {
                "id": 7,
                "age": 43,
                "gender": "M",
                "last_login": datetime(2022, 9, 1, 17, 30, 0),
            },
            {
                "id": 9,
                "age": 13,
                "gender": "M",
                "last_login": datetime(2022, 9, 1, 18, 30, 0),
            },
            {
                "id": 10,
                "age": 63,
                "gender": "M",
                "last_login": datetime(2022, 9, 1, 19, 30, 0),
            },
        ]

        # case_1
        # 요청 항목 1개
        type_list = [1]
        result = dataprocess.calc_user_data(user_data, type_list)
        exp = {
            "gender/all_user": [
                {"gender": "female", "count": 5, "percentage": 50.0},
                {"gender": "male", "count": 5, "percentage": 50.0},
            ]
        }
        self.assertEqual(result, exp)

        # case_2
        # 요청 항목 3개
        type_list = [1, 2, 6]
        result = dataprocess.calc_user_data(user_data, type_list)
        exp = {
            "gender/all_user": [
                {"gender": "female", "count": 5, "percentage": 50.0},
                {"gender": "male", "count": 5, "percentage": 50.0},
            ],
            "age/all_user": [
                {"age_category": 10, "count": 2, "percentage": 20.0},
                {"age_category": 20, "count": 2, "percentage": 20.0},
                {"age_category": 30, "count": 2, "percentage": 20.0},
                {"age_category": 40, "count": 2, "percentage": 20.0},
                {"age_category": 50, "count": 1, "percentage": 10.0},
                {"age_category": 60, "count": 1, "percentage": 10.0},
            ],
            "hour/all_user": [
                {"time_category": 10, "count": 1, "percentage": 10.0},
                {"time_category": 11, "count": 1, "percentage": 10.0},
                {"time_category": 12, "count": 1, "percentage": 10.0},
                {"time_category": 13, "count": 1, "percentage": 10.0},
                {"time_category": 14, "count": 1, "percentage": 10.0},
                {"time_category": 15, "count": 1, "percentage": 10.0},
                {"time_category": 16, "count": 1, "percentage": 10.0},
                {"time_category": 17, "count": 1, "percentage": 10.0},
                {"time_category": 18, "count": 1, "percentage": 10.0},
                {"time_category": 19, "count": 1, "percentage": 10.0},
            ],
        }
        self.assertEqual(result, exp)
        # case_3
        # 요청 항목 6개
        type_list = [1, 2, 3, 4, 5, 6]
        result = dataprocess.calc_user_data(user_data, type_list)
        exp = {
            "gender/all_user": [
                {"gender": "female", "count": 5, "percentage": 50.0},
                {"gender": "male", "count": 5, "percentage": 50.0},
            ],
            "age/all_user": [
                {"age_category": 10, "count": 2, "percentage": 20.0},
                {"age_category": 20, "count": 2, "percentage": 20.0},
                {"age_category": 30, "count": 2, "percentage": 20.0},
                {"age_category": 40, "count": 2, "percentage": 20.0},
                {"age_category": 50, "count": 1, "percentage": 10.0},
                {"age_category": 60, "count": 1, "percentage": 10.0},
            ],
            "age&gender/all_user": [
                {
                    "gender": "female",
                    "age_category": 10,
                    "count": 1,
                    "percentage": 10.0,
                },
                {
                    "gender": "female",
                    "age_category": 20,
                    "count": 1,
                    "percentage": 10.0,
                },
                {
                    "gender": "female",
                    "age_category": 30,
                    "count": 1,
                    "percentage": 10.0,
                },
                {
                    "gender": "female",
                    "age_category": 40,
                    "count": 1,
                    "percentage": 10.0,
                },
                {
                    "gender": "female",
                    "age_category": 50,
                    "count": 1,
                    "percentage": 10.0,
                },
                {"gender": "male", "age_category": 10, "count": 1, "percentage": 10.0},
                {"gender": "male", "age_category": 20, "count": 1, "percentage": 10.0},
                {"gender": "male", "age_category": 30, "count": 1, "percentage": 10.0},
                {"gender": "male", "age_category": 40, "count": 1, "percentage": 10.0},
                {"gender": "male", "age_category": 60, "count": 1, "percentage": 10.0},
            ],
            "age/all_male_user": [
                {"age_category": 10, "count": 1, "percentage": 20.0},
                {"age_category": 20, "count": 1, "percentage": 20.0},
                {"age_category": 30, "count": 1, "percentage": 20.0},
                {"age_category": 40, "count": 1, "percentage": 20.0},
                {"age_category": 60, "count": 1, "percentage": 20.0},
            ],
            "age/all_female_user": [
                {"age_category": 10, "count": 1, "percentage": 20.0},
                {"age_category": 20, "count": 1, "percentage": 20.0},
                {"age_category": 30, "count": 1, "percentage": 20.0},
                {"age_category": 40, "count": 1, "percentage": 20.0},
                {"age_category": 50, "count": 1, "percentage": 20.0},
            ],
            "hour/all_user": [
                {"time_category": 10, "count": 1, "percentage": 10.0},
                {"time_category": 11, "count": 1, "percentage": 10.0},
                {"time_category": 12, "count": 1, "percentage": 10.0},
                {"time_category": 13, "count": 1, "percentage": 10.0},
                {"time_category": 14, "count": 1, "percentage": 10.0},
                {"time_category": 15, "count": 1, "percentage": 10.0},
                {"time_category": 16, "count": 1, "percentage": 10.0},
                {"time_category": 17, "count": 1, "percentage": 10.0},
                {"time_category": 18, "count": 1, "percentage": 10.0},
                {"time_category": 19, "count": 1, "percentage": 10.0},
            ],
        }
        self.assertEqual(result, exp)


# unittest를 실행
if __name__ == "__main__":
    unittest.main()
