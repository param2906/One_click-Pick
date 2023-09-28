from django.shortcuts import render, redirect
from user.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from authentication.views.otp import generate_otp
from authentication.helpers import send_verification_otp


class Login(View):
    template_name = 'account/login.html'
    # form_class = Loginform
    def get(self,request):
        return render(request, self.template_name)
    def post(self,request):
        message = ''
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            if(user.is_active == False):
                otp = generate_otp()
                user.otp = otp
                user.save()
                User.objects.filter(email=email).update(is_active =False)
                send_verification_otp(email, otp)
                context = {
                    'email' :email,
                }
                return render(request,'account/otp.html',context)
            else:
                if check_password(password,user.password):
                    login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                    return redirect('index')
                else:
                    messages.error(request,'password is wrong')
        else:
            messages.error(request,'no user found')
        return render(request, self.template_name)
    
# class Profile(View):
#     def get(self,request):
#         return render(request,'products/index.html')

