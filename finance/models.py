from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    ]
    
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    amount = models.DecimalField(max_digits= 10, decimal_places = 2)
    transaction_type = models.CharField(max_length = 10, choices = TRANSACTION_TYPE)
    date = models.DateField()
    category = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    target_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    deadline = models.DateField()
