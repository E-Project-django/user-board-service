from django.db import models

from core.models import TimeStampModel


class Freeboard(TimeStampModel):
    """
     추상화 기초클래스인 TimeStampedModel를 상속하였다.
     TimeStampedModel의 'create_time', 'update_time'필드가 Freeboard 모델에 포함된다.
     """
    title = models.CharField(max_length=100)
    content = models.TextField()
    author_id = models.ForeignKey(
        'accounts.User', null=True, on_delete=models.SET_NULL, db_column='author_id', related_name='freeboard')
    # 사용자의 계정이 삭제되어도 작성자는 NULL로 변경되고 게시글은 보존되도록

    class Meta:
        db_table = 'freeboard'

    def __str__(self):
        return self.title


class Notice(TimeStampModel):
    """
     추상화 기초클래스인 TimeStampedModel를 상속하였다.
     TimeStampedModel의 'create_time', 'update_time'필드가 Notice 모델에 포함된다.
     """
    title = models.CharField(max_length=100)
    content = models.TextField()
    author_id = models.ForeignKey(
        'accounts.User', null=True, on_delete=models.SET_NULL, db_column='author_id', related_name='notice')

    class Meta:
        db_table = 'notice'

    def __str__(self):
        return self.title


class Staffboard(TimeStampModel):
    """
     추상화 기초클래스인 TimeStampedModel를 상속하였다.
     TimeStampedModel의 'create_time', 'update_time'필드가 Staffboard 모델에 포함된다.
     """
    title = models.CharField(max_length=100)
    content = models.TextField
    author_id = models.ForeignKey(
        'accounts.User', null=True, on_delete=models.SET_NULL, db_column='author_id', related_name='staffboard')

    class Meta:
        db_table = 'staffboard'

    def __str__(self):
        return self.title
