from django.core.validators import MinValueValidator
from django.db import models

from shop.models.base_model import BaseModel
from shop.models.cart.cart import Cart
from shop.models.product.product import Product


class CartProducts(BaseModel):
    price_per_item = models.IntegerField(validators=[MinValueValidator(0)])
    count = models.IntegerField(validators=[MinValueValidator(0)])
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
