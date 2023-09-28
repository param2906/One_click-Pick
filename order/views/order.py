from django.shortcuts import render
from django.views import View
from user.models import User
from order.models import Order, OrderItem
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required(login_url='/account/login'), name='dispatch')
class Orders(View):
    def get(self,request,pk):
        user = User.objects.get(id=pk)
        order = Order.objects.filter(user=user , paid = True).order_by('-id')
        orderitem = OrderItem.objects.filter(order__in =order)
        context = {
            'order' : order,
            'orderitem' : orderitem
        }
        return render(request,'order/order.html',context)
    