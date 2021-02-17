from django.db import models
from shop.model.base_model import BaseModel


class CartProducts(BaseModel):
    price_per_item = models.IntegerField()
    count = models.IntegerField()

    # TODO: Foreign key to product and cart tables
    # product_id =
    # cart_id =
