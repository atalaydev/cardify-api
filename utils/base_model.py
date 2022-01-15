from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_by = models.ForeignKey(
        User,
        blank=False,
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_created_by'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
