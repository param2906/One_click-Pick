from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from authentication.forms import checkpassword
from user.models import User

class Resetpassword(View):
    def get(self,request):
        return render(request,'account/resetpassword.html')
    def post(self,request):
        password = request.POST.get('currentpassword')
        newpassword = request.POST.get('newpassword')
        confirmpassword = request.POST.get('confirmpassword')
        user = request.user
        email = User.objects.get(email=user)
        print(user)
        if(check_password(password,user.password)):
            
            if (len(newpassword) < 8):
                messages.error(request, "password is short")
                return render(request, 'account/resetpassword.html')
            else:
                if(checkpassword(newpassword)==True):
                    if newpassword != confirmpassword:
                        messages.error(request, "both password should be same")
                        return render(request, 'account/resetpassword.html')
                    messages.success(request,'your password has been changed')
                    email.set_password(newpassword)
                    email.save()
                    return redirect('customer_login')
        else:
            messages.error(request,'Current passowrd is wrong')        

        return render(request,'account/resetpassword.html')