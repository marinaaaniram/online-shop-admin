from django.db import models

from products.models import Product


class Order(models.Model):
    INIT = 'init'
    IN_PROGRESS = 'in_progress'
    CONFIRMED = 'confirmed'
    STATUS_CHOICES = (
        (INIT, 'Init'),
        (IN_PROGRESS, 'In progress'),
        (CONFIRMED, 'Confirmed'),
    )

    products = models.ManyToManyField(Product)
    order_sum = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=INIT)
    confirmed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
