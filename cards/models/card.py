import uuid
from django.db import models


class Card(models.Model):
    
    class CardStatus(models.IntegerChoices):
        NEW = 0
        ON_GOING = 1
        DONE = 2

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    front = models.TextField(max_length=256, blank=False, verbose_name='Front-face')
    back = models.TextField(max_length=256, blank=False, verbose_name='Back-face')
    streak = models.IntegerField(default=0, blank=False)
    status = models.IntegerField(choices=CardStatus.choices, default=CardStatus.NEW)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
