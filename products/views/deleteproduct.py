from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView
from products.models import Products
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@method_decorator(login_required(login_url='/account/login'), name='dispatch')
class DeleteProduct(DeleteView):
    def get(self,request,pk):
        products = Products.objects.get(id=pk)  
        products.delete()
        messages.success(request,'Product has been deleted successfully ')
        return redirect('products')
        # return HttpResponseRedirect(reverse('products'))
