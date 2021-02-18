from django.db import models
from shop.model.base_model import BaseModel


class OrderProducts(BaseModel):
    price_per_item = models.IntegerField()
    count = models.IntegerField()
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)
