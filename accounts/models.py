from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# 사용자 모델
class User(AbstractUser):
    """
     AbstractUser에서 'id, username, first_name, last_name, password, email, is_staff, is_active, date_joined'를 상속받는다.
     추가로 'age, gender, phone_number'를 정의하였다.
    """
    CHOICES_GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    age = models.PositiveIntegerField(null=False, blank=False)
    gender = models.CharField(max_length=1, choices=CHOICES_GENDER, null=False, blank=False)
    phoneNumberRegex = RegexValidator(regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone_number = models.CharField(validators=[phoneNumberRegex], max_length=13, unique=True,
                                    help_text="Please use the following format: 010-1234-5678")

    REQUIRED_FIELDS = ['age', 'gender', 'phone_number']

    def __str__(self):
        return self.username
