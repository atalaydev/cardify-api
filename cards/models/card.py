import uuid
from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    
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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    front = models.TextField(max_length=256, blank=False, verbose_name='Front-face')
    back = models.TextField(max_length=256, blank=False, verbose_name='Back-face')
    streak = models.IntegerField(default=0, blank=False)
    status = models.IntegerField(choices=CardStatus.choices, blank=False, default=CardStatus.ACTIVE)
    confidence = models.IntegerField(choices=ConfidenceLevel.choices, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, blank=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)
