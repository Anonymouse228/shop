from django.db import models
from shop.model.base_model import BaseModel


class Manufacturer(BaseModel):
    name = models.CharField(max_length=255)
