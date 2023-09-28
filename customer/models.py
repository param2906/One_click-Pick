from django.db import models
from user.models import User
from products.models import Products
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='user.cart+')
    # quantity = models.IntegerField(null=True)
    total_price = models.DecimalField(null=True,decimal_places=2,max_digits=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User, null=True,blank=True,related_name='user.cart.created_by+',on_delete=models.SET_NULL)
    update_by=models.ForeignKey(User,max_length=200, null=True,related_name='user.cart.updated_by+' ,blank=True,on_delete=models.SET_NULL)


class CartItem(models.Model):
    product = models.ForeignKey(Products,null=True,on_delete=models.SET_NULL,related_name='cartitem+')
    cart = models.ForeignKey(Cart,null=True,on_delete=models.SET_NULL,related_name='cart+')
    size = models.CharField(null=True,blank=True,max_length=5)
    colour = models.CharField(null=True,blank=True,max_length=20)
    quantity = models.IntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User, null=True,blank=True,related_name='user.cartitem.created_by+',on_delete=models.SET_NULL)
    update_by=models.ForeignKey(User,max_length=200, null=True,related_name='user.cartitem.updated_by+' ,blank=True,on_delete=models.SET_NULL)


    # def __str__(self):
    #     # return self.product.name