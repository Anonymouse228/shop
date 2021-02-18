from django.core.validators import MinValueValidator
from django.db import models

from shop.models.product.product import Product
from shop.models.order.order import Order
from shop.models.base_model import BaseModel


class OrderProducts(BaseModel):
    price_per_item = models.IntegerField(validators=[MinValueValidator(0)])
    count = models.IntegerField(validators=[MinValueValidator(0)])
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
