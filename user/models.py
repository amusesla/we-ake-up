from django.db import models

# Create your models here.


class TimestampedModel(models.Model):
    """ 시간 추상 클래스

    History:
        2021-02-11: 초기생성
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(TimestampedModel):
    """ 유저모델

    History:
        2021-02-11: 초기생성
    """
    username = models.CharField(max_length=10)
    code = models.PositiveSmallIntegerField(null=True)
    is_staff = models.BooleanField(default=False)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username
