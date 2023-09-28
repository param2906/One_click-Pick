from django.shortcuts import render,HttpResponseRedirect
from order.forms import OrderForm
from django.views import View
from django.urls import reverse
from customer.models import Cart, CartItem
from order.models import  OrderItem
from django.shortcuts import  render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required(login_url='/account/login'), name='dispatch')
class Checkout(View):
    def get(self,request,pk):
        cart  = Cart.objects.get(id = pk)
        form = OrderForm(instance=cart.user)
        context = {
            'form':form,
        }
        return render(request,'order/checkout.html',context)

    def post(self,request,pk):
        cart = Cart.objects.get(id = pk)
        cartitem = CartItem.objects.filter(cart=cart)
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = cart.user
            order.total_price = cart.total_price
            order.save()
            for i in cartitem:
                orderitem = OrderItem(product = i.product, order = order,size =i.size, colour=i.colour,quantity=i.quantity)
                orderitem.save()    
            cartitem.delete()
            return HttpResponseRedirect(reverse('payment',args=[order.id]))
        context = {
            'form':form,
            'order':order
        }
        return render(request,'order/checkout.html',context)