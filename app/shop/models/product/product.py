from django.core.validators import MinValueValidator
from django.db import models

from shop.models.product.category import Category
from shop.models.product.manufacturer import Manufacturer
from shop.models.base_model import BaseModel


class Product(BaseModel):
    title = models.CharField(max_length=255)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField()
    visible = models.BooleanField(default=True)
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
