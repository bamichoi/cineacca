from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """TimeStampledModel Definition"""  # 오브젝트 생성, 업데이트 시간이 필요한 모델들을 위해 TimeStampedModel을 abstract로 생성.

    create = models.DateTimeField(
        auto_now_add=True
    )  # auto_now_add 는 생성될때만 시간을 업데이트 한다.
    updated = models.DateTimeField(auto_now=True)  # auto_now 는 수정될 때마다 시간을 업데이트 한다.

    class Meta:
        abstract = True
