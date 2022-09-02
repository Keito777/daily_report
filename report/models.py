from django.db import models

# 作成日時、更新日時fieldを定義したモデル
# このモデルを継承することで2つのfieldの定義を省略することができる
from model_utils.models import TimeStampedModel

class Post(TimeStampedModel):
    # created = models.DateTimeField(auto_now_add=True)　新規作成
    # modified = models.DateTimeField(auto_now=True) 更新
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title

