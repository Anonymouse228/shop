from django.db import models
from shop.model.base_model import BaseModel


class Order(BaseModel):
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=None)

    # TODO: Foreign key to user table
    # user =
