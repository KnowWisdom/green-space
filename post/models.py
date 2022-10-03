from statistics import mode
from django.db import models
from users.models import CustomUser

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="items", null=False)
    text = models.TextField()
    user = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
        related_name = "posts",
        related_query_name = "post"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    accepted = models.BooleanField(default=False)