from django.db import models
from shop.model.base_model import BaseModel


class Cart(BaseModel):
    price = models.IntegerField()
    _user = models.ForeignKey('User', on_delete=models.CASCADE)
