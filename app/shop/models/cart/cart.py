from django.core.validators import MinValueValidator
from django.db import models

from shop.models.base_model import BaseModel
from shop.models.customer.customer import Customer


class Cart(BaseModel):
    price = models.IntegerField(validators=[MinValueValidator(0)])
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
