from django.db import models
from api.user.models import CustomUser
from api.product.models import ProductModel


class OrderModel(models.Model):
    transaction_id = models.CharField(max_length=200, default=0)
    product_names = models.CharField(max_length=800)
    total_amount = models.CharField(max_length=50, default=0)
    total_products = models.CharField(max_length=500, default=0)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
