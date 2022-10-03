from random import choices
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Register
class CustomAccountManger(BaseUserManager):
    def create_superuser(self, nickname, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')
        return self.create_user(nickname, username, password, **extra_fields)

    def create_user(self, nickname, username, password, **extra_fields):
        if not nickname:
            raise ValueError(_('You must provide an nickname'))

        user = self.model(
            nickname=nickname, username=username, 
            password=password, phone=extra_fields.pop('phone', None),
            **extra_fields
        )
        user.set_password(password)
        user.save()

class CustomUser(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'None'),
    )
    
    user_id = models.BigAutoField(
        primary_key=True,
        unique=True,
        editable=False,
        verbose_name='user_id',
    )
    username = models.CharField(max_length=45, ) # 닉네임
    nickname = models.CharField(max_length=45, unique=True) # 아이디
    create_dt = models.DateTimeField(default=timezone.now, blank=True, null=True) 
    phone = models.CharField(max_length=45, blank=True, null=True) 
    gender = models.CharField(max_length = 200, choices=GENDER_CHOICES, default='N')
    age = models.IntegerField(null=True, blank=True)

    open = models.BooleanField(default=True)

    point = models.IntegerField(default=0)

    # like_products = models.ManyToManyField('Product', blank=True, related_name='like_users')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManger()

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['username'] 

    class Meta:
        db_table = 'users'
        verbose_name = _('user')
        verbose_name_plural = _('users')
        
    def __str__(self):
        return self.username



class Follow(models.Model):
    class Meta:
        unique_together = ('user', 'following')

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    following = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='following')