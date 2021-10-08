from django.db import models
from django.utils import timezone

from .customer import Order

class Payment(models.Model):
    paymentId = models.BigAutoField(null=False,primary_key=True)
    orderDetails = models.ForeignKey(Order)
    orderTime = models.DateTimeField(default=timezone.now)
    isPaymentSuccess = models.BooleanField(default=False)