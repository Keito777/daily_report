from django.db import models

# 作成日時、更新日時fieldを定義したモデル
# このモデルを継承することで2つのfieldの定義を省略することができる
from model_utils.models import TimeStampedModel

class Post(TimeStampedModel):
    # created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
    # modified_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title

