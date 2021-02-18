from django.db import models
from shop.model.base_model import BaseModel


class CartProducts(BaseModel):
    price_per_item = models.IntegerField()
    count = models.IntegerField()
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    cart_id = models.ForeignKey('Cart', on_delete=models.CASCADE)
