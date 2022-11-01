from contextlib import nullcontext
from email.policy import default
from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# 녹색 공간 꾸밀 아이템
class Item(models.Model):

    CATEGORY_CHOICES = (
        ('item1', 'item1'),
        ('item2', 'item2'),
        ('badge', 'badge'),
    )

    id = models.BigAutoField(
        primary_key=True, 
        unique=True, 
        verbose_name="item_id"
    )

    name = models.CharField(max_length = 200, null=True)

    image = models.ImageField(upload_to="items", null=False)

    point = models.IntegerField(default=10)

    category = models.CharField(max_length = 200, choices=CATEGORY_CHOICES, default='N')

    def __str__(self) :
        return self.name

# 구매한 아이템과 배지
class Buy(models.Model):

    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
    )

    pick = models.BooleanField(default=False)