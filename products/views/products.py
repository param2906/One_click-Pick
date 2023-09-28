from django.shortcuts import render
from django.views import View
from products.models import Products
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
@method_decorator(login_required(login_url='/account/login'), name='dispatch')
class UserProducts(View):
    def get(self,request):
        user = request.user
        
        products = Products.objects.filter(created_by=user) 
        paginator_product = Paginator(products,6) 
        page_number = request.GET.get('page')
        page_obj = paginator_product.get_page(page_number)
        context = {
            'products' : products,  
            'page_obj' : page_obj,
        }
        return render(request,'products/products.html',context)