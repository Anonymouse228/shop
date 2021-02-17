from django.db import models
from shop.model.base_model import BaseModel


class Product(BaseModel):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    visible = models.BooleanField(default=True)
    amount = models.IntegerField()

    # TODO: Foreign key to category and manufacturer tables
    # category =
    # manufacturer =
