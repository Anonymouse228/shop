from django.db import models
from shop.model.base_model import BaseModel


class Review(BaseModel):
    rating = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    # TODO: Foreign key to product and user tables
    # product =
    # user =
