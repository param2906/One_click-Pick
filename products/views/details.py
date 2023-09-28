from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from products.models import Products
from django.contrib import messages
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django.core import serializers
from django.contrib.auth.decorators import login_required
from customer.models import Cart,CartItem
@method_decorator(login_required(login_url='/account/login'), name='dispatch')
class Details(View):
    def get(self,request,pk):
        products = Products.objects.get(id=pk)
        likesproduct = Products.objects.filter(category=products.category)
        color = products.colour.all()
        size = products.size.all()
        context = {
            'products' : products,
            'likesproduct'  :likesproduct,
            'color' : color,
            'size' : size,
        }
        return render(request,'products/shopdetail.html',context)
    def post(self,request,pk):
        products = Products.objects.get(id=pk)
        # cartitem = CartItem.objects.filter(product=products).values_list('product', flat=True)
        cartitem = CartItem.objects.filter(product=products)
        user = request.user
        cart = Cart.objects.get(user = user)
        clothsize = request.POST['clothsize']
        if not clothsize:
            return JsonResponse({"message":"please select the size"})
        clothcolor = request.POST['clothcolor']
        
        if not clothcolor:
            return JsonResponse({"message":"please select the color"})
        quantity = request.POST['quantity']
        count=1
        if cartitem:
            for i in cartitem:
                if products.id ==i.product.id and cart.id ==i.cart.id: 
                    if i.size == clothsize and i.colour == clothcolor:
                        count+=1
                        return JsonResponse({"message":"product is already in cart"})
        count=0           
        if count == 0:
            ci = CartItem(cart=cart,product=products,size=clothsize,colour=clothcolor,quantity=quantity)
            ci = CartItem.objects.create(
                cart = cart,
                product = products,
                size = clothsize,
                colour = clothcolor,
                quantity = quantity,
            )
            ci.save()
            return JsonResponse({"message":"product is added to cart"})
        return JsonResponse({"message":""})
