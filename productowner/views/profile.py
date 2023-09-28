from django.shortcuts import render,redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from productowner.forms import ProfileForm
from user.models import User
from django.contrib import messages

@method_decorator(login_required(login_url='/account/login'), name='dispatch')
class ProductOwnerProfile(View):
    def get(self,request,pk): 
        print(pk)
        user = User.objects.get(id = pk)
        form = ProfileForm(instance=user)
        context = {
            'form' : form,
        }
        return render(request,'productowner/profile.html',context)
    def post(self,request,pk):
        user = User.objects.get(id = pk)
        form = ProfileForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            # user = form.save(commit=False)
            address = form.cleaned_data.get('address')
            profile = form.cleaned_data.get('profile')
            # print(email)
            user.address = address
            user.profile = profile
            user.update_by = user.email
            user.save()
            messages.success(request,'Profile is successfully updated')
            return redirect('index')
        context = {
            'form' : form
        }
        return render(request,'productowner/profile.html',context)