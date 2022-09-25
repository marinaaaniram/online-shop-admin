from django.db import models
from django.db.models import CASCADE

from orders.models import Order


class Payment(models.Model):
    INIT = 'init'
    PAID = 'paid'
    STATUS_CHOICES = (
        (INIT, 'Init'),
        (PAID, 'Paid'),
    )

    CASH = 'cash'
    NON_CASH = 'non_cash'
    PAYMENT_TYPE_CHOICES = (
        (CASH, 'cash'),
        (NON_CASH, 'Non cash'),
    )

    order = models.OneToOneField(Order, on_delete=CASCADE)
    payment_sum = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=INIT)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES, default=NON_CASH)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super(Payment, self).__init__(*args, **kwargs)
        self.old_status = self.status

    def save(self, *args, **kwargs):
        if self.old_status == self.PAID:
            self.status = self.PAID
        super(Payment, self).save(*args, **kwargs)
