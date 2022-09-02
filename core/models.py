from django.db import models


class TimeStampModel(models.Model):
    """
     'created'와 'modified'필드를 자동으로 업데이트해 주는 추상화 기반 클래스 모델
     """
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True