from django.urls import reverse
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from customer.models import Cart,CartItem
from user.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

@method_decorator(login_required(login_url='/account/login'), name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class Deletecartitem(DeleteView):
    def get(self,request,pk):
        user = request.user
        id  = str(user.id)
        cartitem = CartItem.objects.get(id=pk)
        cartitem.delete()
        messages.success(request,'Product has been removed successfully')
        return HttpResponseRedirect(reverse('showcart', args=[id]))
    