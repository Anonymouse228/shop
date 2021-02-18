from django.db import models
from shop.model.base_model import BaseModel


class Product(BaseModel):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    visible = models.BooleanField(default=True)
    amount = models.IntegerField()
    _category = models.ForeignKey('Category', on_delete=models.CASCADE)
    _manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
