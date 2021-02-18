from django.db import models


class DiscountUser(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    discount_id = models.ForeignKey('Discount', on_delete=models.CASCADE)
