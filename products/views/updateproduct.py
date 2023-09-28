from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import UpdateView
from products.models import Products,Colour,Category,Size
from products.forms import ProductForm
from django.contrib import messages
from django.utils.decorators import method_decorator    
from django.contrib.auth.decorators import login_required

@method_decorator(login_required(login_url='/account/login'), name='dispatch')
class UpdateProduct(UpdateView):
    def get(self,request,pk):
        form = ProductForm()
        products = Products.objects.get(id=pk)
        form = ProductForm(instance=products)
        
        context = {
            'form' : form,
            'name' : 'Update Product',
        }
        return render(request,'products/createProduct.html',context)
    def post(self,request,pk):
        products = Products.objects.get(id=pk)
        colors = request.POST.getlist('colour')
        size = request.POST.getlist('size') 
        category = request.POST.get('category')
        if category:
            category = Category.objects.get(id = category)
        form = ProductForm(request.POST,request.FILES,instance=products)
        input_color = request.POST.get('addcolor')
        if input_color:
            if Colour.objects.filter(name = input_color).exists():
                messages.error(request,'color is already exists')
                return HttpResponseRedirect(reverse('updateproduct',args=[products.id]))
            else:
                Colour.objects.create(name=input_color)
                messages.success(request,'color is added successfully')
                return HttpResponseRedirect(reverse('updateproduct',args=[products.id]))
        input_category = request.POST.get('addcategory')
        if input_category:
            if Category.objects.filter(name = input_category).exists():
                messages.error(request,'category is already exists')
                return HttpResponseRedirect(reverse('updateproduct',args=[products.id]))
            else:
                Category.objects.create(name=input_category)
                messages.success(request,'category is added successfully')
                return HttpResponseRedirect(reverse('updateproduct',args=[products.id]))
        input_size = request.POST.get('addsize')
        if input_size:
            if Size.objects.filter(name = input_size).exists():
                messages.error(request,'size is already exists')
                return HttpResponseRedirect(reverse('updateproduct',args=[products.id]))
            else:
                Size.objects.create(name=input_size)
                messages.success(request,'size is added successfully')
                return HttpResponseRedirect(reverse('updateproduct',args=[products.id]))
            
        user = request.user
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = user
            product.category = category
            product.save()
            product.colour.set(colors)
            product.size.set(size)
            product.category = category
            messages.success(request,'product has been updated successfully created')
            return redirect('index')
        context = {
            'form':form,
            'name' : 'Update Product',
        }
        return render(request,'products/createProduct.html',context)
