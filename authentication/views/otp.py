from user.models import User
from django.views import View
from django.shortcuts import render,redirect
from django.contrib import messages
from authentication.helpers import send_verification_otp
# from register import val
import math
import random


def generate_otp():
    digits = "123456789"
    otp = ""
    i=0
    for i in range(4): 
        otp+=digits[math.floor(random.random()*10)]
    otp = int(otp)
    return int(otp)

class Otp(View):
    def get(self,request):
        
        return render(request,'account/otp.html')
    
    def post(self,request):
        realotp = request.POST.get('otp')
        # realotp = request.POST.get('realotp')
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
        else:
            messages.error(request,'User is not found')
            return redirect ('registrationOtp')
        # print(realotp)

        # clickbutton = request.POST.get('submit')
        if 'resendotp' in request.POST:
            otp = generate_otp()
            User.objects.filter(email=email).update(otp = otp)
            send_verification_otp(email, otp)
        if 'submit' in request.POST:
            if realotp:
                otp = user.otp
                print(type(otp))
                print(realotp)
                if(otp == int(realotp)):
                    user = User.objects.get(otp=otp)
                    user.is_active = True
                    user.save()
                    messages.success(request,'user successfully created')
                    return redirect('customer_login')
                else:
                    messages.error (request,'Otp is wrong please try again')
            context = {    
            'email' : email,
            }
            return render(request,'account/otp.html',context)
        messages.error (request,'Email has been sent')
        context = {  
            'email' : email,
        }
        return render(request,'account/otp.html',context)
        

