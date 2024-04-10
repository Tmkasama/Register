from django.db import models

class TaskListModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)

class DeliveryModel(models.Model):
    local_drop_off = models.BooleanField(default=False)
    local_pick_up = models.BooleanField(default=False)
    shopping = models.BooleanField(default=False)
    ship_N = models.CharField(max_length=10)
    ship_date = models.DateField()

class PaymentModel(models.Model):
    cash = models.BooleanField()
    card = models.BooleanField()
    checks = models.BooleanField()
    paypal = models.BooleanField()
    other = models.BooleanField()

class AmountModel(models.Model):
    Subtotal = models.CharField(max_length=100)
    Taxes = models.CharField(max_length=100)
    Shipping = models.CharField(max_length=100)
    Total = models.CharField(max_length=100)

