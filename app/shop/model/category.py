from django.db import models
from shop.model.base_model import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE)
