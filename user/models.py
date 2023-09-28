from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, null=True, db_index=True)
    phone=models.CharField(max_length=10, null=True,blank=True)
    address=models.TextField(max_length=200,null=True,blank=True)
    profile=models.ImageField(default="profile.png",null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    otp=models.IntegerField(null=True,blank=True)
    forget_password_token = models.CharField(max_length=100,null=True,blank=True)
    is_active=models.BooleanField(default=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.CharField(max_length=200, null=True,blank=True)
    update_by=models.CharField(max_length=200, null=True,blank=True)

    
    
    REQUIRED_FIELDS =[]
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email
