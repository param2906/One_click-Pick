from django.shortcuts import render
from django.views import View
from products.models import Products,Section
from django.db.models import Q
from customer.models import Cart
from user.models import User

class Index(View):
    def get(self,request):
    #    u = User.objects.get(email=request.user)
    #    print(u.Cart_set.all().count()) 
       cart  = Cart.objects.all()
       u = request.user
       count =0
       for i in cart:
           if u == i.user:
               count=1
               break
       if count == 0:
            Cart.objects.create(
                user = u
            )
       section = Section.objects.all()
       product = Products.objects.all()
       products = Products.objects.order_by('-created_at')
       s = request.GET.get('search')
       pr = None
       if s is not None:
           pr = product.filter(Q(name__icontains=s) | Q(company__icontains=s))
       context = {
           'section' : section,
           'products' : products,
           'pr' : pr,
           's':s,
       }
       return render(request,'products/index.html',context)