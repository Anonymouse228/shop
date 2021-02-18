from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from shop.models.base_model import BaseModel
from shop.models.file.file import File
from shop.models.discount.discount import Discount


class Customer(BaseModel, AbstractBaseUser):
    discounts = models.ManyToManyField(Discount)
    photo = models.OneToOneField(File, on_delete=models.CASCADE)
