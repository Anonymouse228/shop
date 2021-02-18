from django.core.validators import MinValueValidator
from django.db import models
from shop.models.base_model import BaseModel


class Discount(BaseModel):
    code = models.CharField(max_length=255)
    value = models.IntegerField(help_text='Discount value int%')
    is_active = models.BooleanField(default=True)
    available_to = models.DateTimeField()
    count = models.IntegerField(validators=[MinValueValidator(0)])
