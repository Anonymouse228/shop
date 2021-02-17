from django.db import models
from shop.model.base_model import BaseModel


class Discount(BaseModel):
    code = models.CharField(max_length=255)
    value = models.IntegerField()
    is_active = models.BooleanField(default=False)
    available_to = models.DateTimeField()
    count = models.IntegerField()
