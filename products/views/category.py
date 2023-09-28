from django.shortcuts import render
from django.views import View
from products.models import Products,Category,Section
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
@method_decorator(login_required(login_url='/account/login'), name='dispatch')
class Category(View):
    
    def get(self,request,pk):
        section = Section.objects.get(id=pk)
        products = Products.objects.filter(section=section)
        
        paginator_product = Paginator(products,6) 
        page_number = request.GET.get('page')
        page_obj = paginator_product.get_page(page_number)
        context = {
            'products' : products,  
            'page_obj' : page_obj,  
            'section' : section,  
        }
        return render(request,'products/category.html',context)
    
