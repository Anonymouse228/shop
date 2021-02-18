from django.core.validators import MinValueValidator
from django.db import models
from shop.models.base_model import BaseModel

from shop.models.customer.customer import Customer


class Order(BaseModel):
    price = models.IntegerField(validators=[MinValueValidator(0)])
    discounted_price = models.IntegerField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def calculate_discounted_price(self, discount: int) -> int:
        return 1
