from django.db import models
from users.models import CustomUser

# Create your models here.

# 녹색 공간 꾸밀 아이템
class Item(models.Model):
    item_id = models.BigAutoField(
        primary_key=True, 
        unique=True, 
        verbose_name="item_id"
    )

    item_name = models.CharField(
        max_length=45, 
        verbose_name="item_name", 
        default="item"
    )

    image = models.ImageField(upload_to="items", null=False)

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

    category_1 = models.ForeignKey(
        Item,
        related_name="category_1",
        on_delete=models.CASCADE,
        null=True,
        db_column="category_1"
    )

    category_2 = models.ForeignKey(
        Item,
        related_name="category_2",
        on_delete=models.CASCADE,
        null=True,
        db_column="category_2"
    )

    category_3 = models.ForeignKey(
        Item,
        related_name="category_3",
        on_delete=models.CASCADE,
        null=True,
        db_column="category_3"
    )

    category_4 = models.ForeignKey(
        Item,
        related_name="category_4",
        on_delete=models.CASCADE,
        null=True,
        db_column="category_4"
    )

    def __str(self):
        return self.owner