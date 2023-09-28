from django.shortcuts import render
from django.views import View
from user.models import User
from customer.models import Cart
from order.forms import OrderForm
from order.models import Order, OrderItem
from django.shortcuts import redirect, render
from django.contrib import messages
import razorpay

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required(login_url='/account/login'), name='dispatch')
class Payment(View):
    def get(self,request,pk):    
        order = Order.objects.get(id = pk)
        cart = Cart.objects.get(user = order.user)
        form = OrderForm(instance=order)
        orderitem = OrderItem.objects.filter(order = order)
        context = {
            'order' : order,
            'form' : form,
            'orderitem' : orderitem,
            'cart':cart,
        }
        return render(request,'order/payment.html',context)
    def post(self,request,pk):
        order = Order.objects.get(id=pk)
        amount = order.total_price * 100
        client = razorpay.Client(auth=("rzp_test_WYD2T6ysRmQIjA", "P40VJloknSaMIwfINX7loxlq"))
        payment =  client.order.create({
                "amount": amount,
                "currency": "INR",
                'payment_capture': '1',
            })
        order.is_placed = True
        order.payment_id = payment['id']
        order.save()
        return render(request,'order/payment.html',{'payment':payment})