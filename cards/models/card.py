import uuid
from django.db import models

from utils.base_model import BaseModel
from buckets.models import Bucket


class Card(BaseModel):
    
    class CardStatus(models.IntegerChoices):
        ARCHIVED = 0
        ACTIVE = 1
        COMPLETED = 2

    class ConfidenceLevel(models.IntegerChoices):
        EXCELLENT = 5
        GOOD = 4
        AVERAGE = 3
        FAIR = 2
        POOR = 1

    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bucket = models.ForeignKey(Bucket, on_delete=models.PROTECT)
    front = models.TextField(max_length=256, blank=False, verbose_name='Front-face')
    back = models.TextField(max_length=256, blank=False, verbose_name='Back-face')
    streak = models.IntegerField(default=0, blank=False)
    status = models.IntegerField(choices=CardStatus.choices, blank=False, default=CardStatus.ACTIVE)
    confidence = models.IntegerField(choices=ConfidenceLevel.choices, blank=False)

    def __str__(self):
        return f'{self.key} ({self.bucket})'
