from django.shortcuts import render
from user.models import User
from django.views.generic.edit import CreateView
from authentication.forms import Registerform
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from authentication.helpers import send_verification_otp
from authentication.views.otp import generate_otp
from customer.models import Cart

class Register(CreateView):
    
    def get(self,request):
        form = Registerform()
        context = {
            'form': form,
        }
        return render(request, 'account/signup.html', context)
    def post(self,request):
        
        form=Registerform(request.POST)
        if form.is_valid():
            password=form.cleaned_data.get('confirm_password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            groups = Group.objects.get(name ='customer')

            user = User.objects.create(

                email = email,
                first_name = first_name,
                last_name = last_name,
                phone = phone,
                password = make_password(password),
                
            )
            user.groups.add(groups)
            otp = generate_otp()
            user.otp = otp
            user.save() 
            User.objects.filter(email=email).update(is_active =False)
            send_verification_otp(email, otp)
            value ={
                'email' : email,
            }
            Cart.objects.create(
                user = user
            )
            # return redirect('registrationOtp')
            messages.success(request,'otp has been sent')   
            return render(request,'account/otp.html',value)   
        context = {
            'form' : form
        }
        
        return render(request, 'account/signup.html', context)
    
class ProductadminRegister(CreateView):
    
    def get(self,request):
        form = Registerform()
        Groups = Group.objects.all()
    
        context = {
            'form': form,
        }
        return render(request, 'account/productAdmin_register.html', context)
    def post(self,request):
        
        form=Registerform(request.POST)
        if form.is_valid():
            password=form.cleaned_data.get('confirm_password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            groups = Group.objects.get(name ='product_admin')

            user = User.objects.create(

                email = email,
                first_name = first_name,
                last_name = last_name,
                password = make_password(password),
                
            )
            user.groups.add(groups) 
            otp = generate_otp()
            user.otp = otp
            user.save()
            User.objects.filter(email=email).update(is_active =False)
            send_verification_otp(email, otp)
            # message = 'Email hass been sent'
            value ={
                'email' : email,
                # 'message' : message
            }
            Cart.objects.create(
                user = user
            )
            # return redirect('registrationOtp')  
            messages.success(request,'otp has been sent') 
            return render(request,'account/otp.html',value)   
        context = {
            'form' : form
        }
        
        return render(request, 'account/productAdmin_register.html', context)



    


