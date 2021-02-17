from django.db import models
from shop.model.base_model import BaseModel


class OrderProducts(BaseModel):
    price_per_item = models.IntegerField()
    count = models.IntegerField()

    # TODO: Foreign key to product and order tables
    # product_id =
    # order_id =
