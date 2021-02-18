from shop.models.base_model import BaseModel
from django.db import models


class File(BaseModel):
    path = models.CharField(max_length=255)
