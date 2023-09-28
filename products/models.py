from django.db import models
from user.models import User

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=100,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User,max_length=200,related_name='products.Section.created_by+', null=True,on_delete=models.SET_NULL)
    update_by=models.ForeignKey(User,max_length=200,related_name='products.Section.ipdated_by+', null=True,blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name

class Colour(models.Model):
    name = models.CharField(max_length=20,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User,max_length=200,related_name='products.colour.created_by+', null=True,on_delete=models.SET_NULL)
    update_by=models.ForeignKey(User,max_length=200,related_name='products.colour.updated_by+', null=True,blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User,max_length=200,related_name='products.category.created_by+', null=True,on_delete=models.SET_NULL)
    update_by=models.ForeignKey(User,max_length=200,related_name='products.Category.ipdated_by+', null=True,blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name
    
class Size(models.Model):
    name = models.CharField(max_length=100,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User,max_length=200,related_name='products.size.created_by+', null=True,on_delete=models.SET_NULL)
    update_by=models.ForeignKey(User,max_length=200,related_name='products.size.ipdated_by+', null=True,blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name

class Products(models.Model):
    
    name = models.CharField(max_length=100,null=True)
    size = models.ManyToManyField(Size,max_length=5,blank=True)  
    company = models.CharField(max_length=100,null=True)
    price = models.FloatField(null=True)
    colour = models.ManyToManyField(Colour,max_length=20,blank=True)
    section = models.ForeignKey(Section,null=True,on_delete=models.SET_NULL)
    category = models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    image = models.ImageField(null=True,blank=True)
    inventory = models.IntegerField(null=True,blank=True)
    multipleimage = models.ImageField(null=True,blank=True)
    description = models.CharField(max_length=500,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User, null=True,blank=True,related_name='User.products.created_by+',on_delete=models.SET_NULL)
    update_by=models.ForeignKey(User,max_length=200, null=True,related_name='user.products.updated_by+' ,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name



    

