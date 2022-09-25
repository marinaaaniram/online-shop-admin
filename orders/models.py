from django.db import models

from products.models import Product


class Order(models.Model):
    INIT = 'init'
    CONFIRMED = 'confirmed'
    STATUS_CHOICES = (
        (INIT, 'Init'),
        (CONFIRMED, 'Confirmed'),
    )

    products = models.ManyToManyField(Product)
    order_sum = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=INIT)
    confirmed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        self.old_status = self.status

    def save(self, *args, **kwargs):
        if self.old_status == self.CONFIRMED:
            self.status = self.CONFIRMED
        super(Order, self).save(*args, **kwargs)

