from django.db import models
from shop.model.base_model import BaseModel


class User(BaseModel):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
