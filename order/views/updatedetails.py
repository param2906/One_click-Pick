from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.views import View
from user.models import User
from order.models import Order, OrderItem
from django.views.generic.edit import UpdateView
from customer.models import Cart
from order.forms import OrderForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required(login_url='/account/login'), name='dispatch')
class Updatedetails(UpdateView):
    def get(self,request,pk):
        cart = Cart.objects.get(id=pk)
        order = Order.objects.filter(user = cart.user).order_by('-id').first()
        orders = Order.objects.get(id = order.id)
        form = OrderForm(instance=orders)
        context = {
            'form' : form
        }
        return render(request,'order/checkout.html',context)
    
    def post(self,request,pk):
        cart = Cart.objects.get(id=pk)
        order = Order.objects.filter(user = cart.user).order_by('-id').first()
        orders = Order.objects.get(id = order.id)
        form = OrderForm(request.POST,instance=orders)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse('payment', args=[orders.id]))
        context = {
            'form' : form
        }    
        return render(request,'order/checkout.html',context)