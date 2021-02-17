from django.db import models
from shop.model.base_model import BaseModel


class Cart(BaseModel):
    price = models.IntegerField()

    # TODO: Foreign key to user table
    # user =
