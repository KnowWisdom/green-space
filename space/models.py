from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# 녹색 공간 꾸밀 아이템
class Item(models.Model):

    item_id = models.BigAutoField(
        primary_key=True, 
        unique=True, 
        verbose_name="item_id"
    )

    image = models.ImageField(upload_to="items", null=False)

    point = models.IntegerField(default=10)

    item_category = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])

# 녹색 공간
class Space(models.Model):
    space_id = models.BigAutoField(
        primary_key=True, 
        unique=True, 
        verbose_name="space_id"
    )

    owner = models.ForeignKey(
        CustomUser, 
        related_name="owner_user", 
        on_delete=models.CASCADE, 
        null=False, 
        db_column="owner"
    )
    
    def __str(self):
        return self.owner


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