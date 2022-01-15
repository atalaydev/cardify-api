import uuid
from django.db import models

from utils.base_model import BaseModel

class Bucket(BaseModel):
    
    class BucketStatus(models.IntegerChoices):
        ARCHIVED = 0
        ACTIVE = 1
        DRAFT = 2

    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80, blank=False, unique=True)
    status = models.IntegerField(choices=BucketStatus.choices, blank=False, default=BucketStatus.DRAFT)

    def __str__(self):
        return f'{self.name} ({self.pk})'
