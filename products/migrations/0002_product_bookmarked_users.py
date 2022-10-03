# Generated by Django 3.2 on 2022-10-03 12:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bookmarked_users',
            field=models.ManyToManyField(related_name='bookmarked_products', to=settings.AUTH_USER_MODEL),
        ),
    ]
