from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from products.models import Colour,Category,Size
from products.forms import ProductForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required(login_url='/account/login'), name='dispatch')
class CreateProduct(CreateView):
    def get(self,request):
        form = ProductForm()
        created_by = {
            'created_by' : request.user,
        }
        form = ProductForm(initial=created_by)
        context = {
            'form' : form,
            'name' : 'Create Product',
        }
        return render(request,'products/createProduct.html',context)
    def post(self,request):
        form = ProductForm(request.POST,request.FILES)
        colors = request.POST.getlist('colour')
        size = request.POST.getlist('size')
        category = request.POST.get('category')
        if category:
            category = Category.objects.get(id = category)
        input_color = request.POST.get('addcolor')
        if input_color:
            if Colour.objects.filter(name = input_color).exists():
                messages.error(request,'color is already exists')
                return redirect('createproduct')
            else:
                Colour.objects.create(name=input_color)
                messages.success(request,'color is added successfully')
                return redirect('createproduct')
        input_category = request.POST.get('addcategory')
        if input_category:
            if Category.objects.filter(name = input_category).exists():
                messages.error(request,'category is already exists')
                return redirect('createproduct')
            else:
                Category.objects.create(name=input_category)
                messages.success(request,'category is added successfully')
                return redirect('createproduct')
        input_size = request.POST.get('addsize')
        if input_size:
            if Size.objects.filter(name = input_size).exists():
                messages.error(request,'size is already exists')
                return redirect('createproduct')
            else:
                Size.objects.create(name=input_size)
                messages.success(request,'size is added successfully')
                return redirect('createproduct')
            
        user = request.user
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = user
            product.category = category
            product.save()
            product.colour.set(colors)
            product.size.set(size)
            product.category = category
            messages.success(request,'product has been created successfully created')
            return redirect('index')
        context = {
            'form':form,
            'name' : 'Create Product',
        }
        return render(request,'products/createProduct.html',context)
