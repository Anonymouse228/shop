from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(default=None)
