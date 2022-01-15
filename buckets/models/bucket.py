import uuid
from django.db import models
from django.contrib.auth.models import User


class Bucket(models.Model):
    
    class BucketStatus(models.IntegerChoices):
        ARCHIVED = 0
        ACTIVE = 1
        DRAFT = 2

    pk = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80, blank=False, unique=True)
    status = models.IntegerField(choices=BucketStatus.choices, blank=False, default=BucketStatus.DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, blank=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name} ({self.pk})'
