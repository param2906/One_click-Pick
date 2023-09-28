from django.shortcuts import render
from django.views import View
from products.models import Products,Category,Size
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from products.filter import CategoryFilter,SectionFilter
from django.db.models import Q
from django.contrib.auth.decorators import login_required
@method_decorator(login_required(login_url='/account/login'), name='dispatch')
class Shop(View):
    
    def get(self,request):
        products = Products.objects.all()
        sizes = Size.objects.all()
        category = Category.objects.all()
        s = request.GET.get('search')
        if s!=None:
            search_product = products.filter(Q(name__icontains=s) | Q(company__icontains=s) )
        else:
            search_product = Products.objects.all()
        
        size = request.GET.getlist('size')

        if size:
            if size == ['allsize']:
                size_product = Products.objects.all()
            else:
                si = Size.objects.filter(name__in=size)
                size_product = Products.objects.filter(size__in=si)
        else:
            size_product = Products.objects.all()
       
        category_filter = CategoryFilter(request.GET,queryset = products)
        section_filter = SectionFilter(request.GET,queryset=products)
        category_products = category_filter.qs
        section_products = section_filter.qs
        search_size_product = search_product.intersection(size_product)
        
        filter_product = category_products.intersection(section_products)
       
        products = filter_product.intersection(search_size_product)
        
        paginator_product = Paginator(products,6) 
        page_number = request.GET.get('page')
        page_obj = paginator_product.get_page(page_number)
        context = {
            'products' : products,  
            'page_obj' : page_obj,  
            'category' : category,  
            'category_filter' : category_filter,
            'section_filter' : section_filter,
            's' : s,
            'sizes' : sizes,
            'size' : size,
        }
        # con['size'] = product.get_size_display()
        return render(request,'products/shop.html',context)
    
