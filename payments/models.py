from django.db import models
from django.db.models import CASCADE

from orders.models import Order


class Payment(models.Model):
    INIT = 'init'
    WAITING = 'waiting'
    PAID = 'paid'
    STATUS_CHOICES = (
        (INIT, 'Init'),
        (WAITING, 'Waiting'),
        (PAID, 'Paid'),
    )

    CASH = 'cash'
    NON_CASH = 'non_cash'
    SUCCESS = 'success'
    PAYMENT_TYPE_CHOICES = (
        (CASH, 'cash'),
        (NON_CASH, 'Non cash'),
    )

    order = models.ForeignKey(Order, on_delete=CASCADE)
    payment_sum = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=INIT)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES, default=NON_CASH)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
