# Generated by Django 3.2 on 2022-11-01 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_buy_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('item', 'item'), ('badge', 'badge')], default='N', max_length=200),
        ),
    ]