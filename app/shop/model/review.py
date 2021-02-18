from django.db import models
from shop.model.base_model import BaseModel


class Review(BaseModel):
    rating = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    _product = models.ForeignKey('Product', on_delete=models.CASCADE)
    _user = models.ForeignKey('User', on_delete=models.CASCADE)
