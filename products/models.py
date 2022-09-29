from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 200)
    company = models.CharField(max_length = 200)
    product_no = models.IntegerField()
    purpose = models.CharField(max_length = 200)

    # like_count = models.PositiveIntegerField(default=0)

    def __str__(self) :
        return self.name
