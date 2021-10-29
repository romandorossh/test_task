import uuid
from django.db import models


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    language = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['created']
