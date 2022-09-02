import pandas as pd
from datetime import datetime


def age_categorize(age):
    """
    유저의 나이를 10단위로 카테고리화
    ex) 25 -> 20

    Args:
        age(int): 유저 나이

    Returns:
        age(int): 카테고리화 한 유저 나이
    """
    age = (age // 10) * 10
    return age


def last_login_categorize(last_login):
    """
    유저의 마지막 로그인 시간을 시간 단위로 카테고리화
    ex) 13:30 -> 13, 14:30 -> 14

    Args:
        last_login (datetime): 유저의 마지막 로그인 시간

    Returns:
        time(int): 카테고리화 유저의 마지막 로그인 시간
    """

    login_hour = datetime.time(last_login).hour
    return login_hour


def calc_ratio(temp_df):
    """
    그룹화 한 데이터 프레임으로 비율을 계산하여 dictionary 형식으로 리턴

    Args:
        temp_df (DataFrame): 필요한 항목으로 그룹화 한 DataFrame

    Returns:
        ratio_dict: 계산된 결과
        ex)
            {
                "gender": "female",
                "count": 3,
                "percentage": 50.0
            },
            {
                "gender": "male",
                "count": 3,
                "percentage": 50.0
            }
    """
    # 비율 계산
    temp_df["percentage"] = round(100 * temp_df["id"] / temp_df["id"].sum(), 2)
    # count로 컬럼명 변경
    temp_df.rename(columns={"id": "count"}, inplace=True)
    # dictionary형으로 변환
    ratio_dict = temp_df.to_dict("records")
    return ratio_dict


def calc_type_gender(user_df):
    """
    집계 기간 내 로그인 유저의 성별 비율을 계산

    Args:
        user_df (DataFrame): 취득한 유저의 데이터 프레임

    Returns:
        result(dict): 계산 결과
    """
    result = {}
    # 성별로 분류
    temp_df = user_df.groupby(["gender"])["id"].count().reset_index()
    # 각 성별 비율 계산
    gender_dict = calc_ratio(temp_df)
    result["gender/all_user"] = gender_dict
    return result


def calc_type_age(user_df):
    """
    집계 기간 내 로그인 유저의 나이대 비율을 계산

    Args:
        user_df (DataFrame): 취득한 유저의 데이터 프레임

    Returns:
        result(dict): 계산 결과
    """
    result = {}
    # 나이대로 분류
    temp_df = user_df.groupby(["age_category"])["id"].count().reset_index()
    # # 각 나이대 비율 계산
    age_dict = calc_ratio(temp_df)
    result["age/all_user"] = age_dict
    return result


def calc_type_gender_age(user_df):
    """
    집계 기간 내 로그인 유저의 성별과 나이대 비율을 계산

    Args:
        user_df (DataFrame): 취득한 유저의 데이터 프레임

    Returns:
        result(dict): 계산 결과
    """
    result = {}
    # 성별과 나이대로 분류
    temp_df = user_df.groupby(["gender", "age_category"])["id"].count().reset_index()
    # 각 성별과 나이대에 따른 비율 계산
    gender_age_dict = calc_ratio(temp_df)
    result["age&gender/all_user"] = gender_age_dict
    return result


def calc_type_male_age(user_df):
    """
    집계 기간 내 로그인 남성 유저의 나이대 비율을 계산

    Args:
        user_df (DataFrame): 취득한 유저의 데이터 프레임

    Returns:
        result(dict): 계산 결과
    """
    result = {}
    # 성별과 나이대로 분류
    temp_df = user_df.groupby(["gender", "age_category"])["id"].count().reset_index()
    temp_df = temp_df[(temp_df["gender"] == "male")]
    temp_df = temp_df.drop(columns=["gender"])
    gender_age_dict = calc_ratio(temp_df)
    result["age/all_male_user"] = gender_age_dict
    return result


def calc_type_female_age(user_df):
    """
    집계 기간 내 로그인 여성 유저의 나이대 비율 계산

    Args:
        user_df (DataFrame): 취득한 유저의 데이터 프레임

    Returns:
        result(dict): 계산 결과
    """
    result = {}
    # female&age
    # 성별과 나이대로 분류
    temp_df = user_df.groupby(["gender", "age_category"])["id"].count().reset_index()
    temp_df = temp_df[(temp_df["gender"] == "female")]
    temp_df = temp_df.drop(columns=["gender"])
    gender_age_dict = calc_ratio(temp_df)
    result["age/all_female_user"] = gender_age_dict
    return result


def calc_type_hour(user_df):
    """
    집계 기간 내 로그인 유저의 각 시간 별 비율 계산

    Args:
        user_df (DataFrame): 취득한 유저의 데이터 프레임

    Returns:
        result(dict): 계산 결과
    """
    result = {}
    # 시간대로 분류
    temp_df = user_df.groupby(["time_category"])["id"].count().reset_index()
    # 각 시간대 비율 계산
    time_dict = calc_ratio(temp_df)
    result["hour/all_user"] = time_dict
    return result


def calc_user_data(users_info, type_list):
    """
    views에서 취득한 유저 정보를 이용하여 요청받은 통계 항목을 계산하여 리턴

    Args:
        users_info (data_set): 취득한 유저 정보 set
        type_list (list): 요청받은 통계 항목 리스트

    Returns:
        result(dict): 각 항목의 통계 결과
    """
    result = {}
    # 데이터 프레임 생성
    user_df = pd.DataFrame(users_info.values())
    # 데이터 전처리
    # gender 값 변환(M = male, F = female)
    user_df["gender"].replace(["M", "F"], ["male", "female"], inplace=True)

    # 나이를 10단위로 카테고리화
    user_df["age_category"] = user_df.age.apply(age_categorize)
    # 시간 단위로 카테고리화
    user_df["time_category"] = user_df.last_login.apply(last_login_categorize)

    # 통계 목록의 수 만큼 루프
    for type in type_list:
        calc_dict = {}
        # 해당 타입에 맞는 통계 실행
        if type == 1:
            # 집계 기간 내 로그인 유저의 성별 비율
            calc_dict = calc_type_gender(user_df)
        elif type == 2:
            # 집계 기간 내 로그인 유저의 나이대 비율
            calc_dict = calc_type_age(user_df)
        elif type == 3:
            # 집계 기간 내 로그인 유저의 성별과 나이대 비율
            calc_dict = calc_type_gender_age(user_df)
        elif type == 4:
            # 집계 기간 내 로그인 남성 유저의 나이대 비율
            calc_dict = calc_type_male_age(user_df)
        elif type == 5:
            # 집계 기간 내 로그인 여성 유저의 나이대 비율
            calc_dict = calc_type_female_age(user_df)
        elif type == 6:
            # 집계 기간 내 로그인 유저의 각 시간 별 비율
            calc_dict = calc_type_hour(user_df)
        else:
            pass
        result.update(calc_dict)

    return result
