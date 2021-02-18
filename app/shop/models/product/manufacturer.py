from django.db import models
from shop.models.base_model import BaseModel


class Manufacturer(BaseModel):
    name = models.CharField(max_length=255, unique=True)
