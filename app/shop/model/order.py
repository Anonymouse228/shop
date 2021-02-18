from django.db import models
from shop.model.base_model import BaseModel


class Order(BaseModel):
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=None)
    _user = models.ForeignKey('User', on_delete=models.CASCADE)
