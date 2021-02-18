from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from shop.models.base_model import BaseModel
from shop.models.product.product import Product
from shop.models.customer.customer import Customer


class Review(BaseModel):
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
