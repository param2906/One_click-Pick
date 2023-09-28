from django.shortcuts import render
from django.views import View
from user.models import User
from order.models import Order, OrderItem
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# @method_decorator(login_required(login_url='/account/login'), name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class Success(View):
    def post(self,request,pk):
        order = Order.objects.get(id=pk)
        orderitem = OrderItem.objects.filter(order=order)
        dict = {
                'orderitem' : orderitem,
                'order' : order,    
            }
        html_template = 'order/orderemail.html'
        html_message = render_to_string(html_template,context=dict)
        subject = 'Order is successfully placed'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [order.user]
        messages = EmailMessage(subject, html_message, email_from, recipient_list)
        messages.content_subtype = 'html'
        messages.send()
        a = request.POST
        
        for key , value in a.items():
            if key =='razorpay_payment_id':
                order.payment_id = value
                order.paid=True
                order.save()   
        return render(request,'order/success.html')