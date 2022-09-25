from django.db import models


class Payment(models.Model):
    INIT = 'init'
    IN_PROGRESS = 'in_progress'
    SUCCESS = 'success'
    STATUS_CHOICES = (
        (INIT, 'Init'),
        (IN_PROGRESS, 'In progress'),
        (SUCCESS, 'Success'),
    )

    payment_sum = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=INIT)
    payment_type = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
