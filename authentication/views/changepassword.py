from user.models import User
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from authentication.forms import checkpassword

class Changepassword(View):
    def get(self, request, token):
        profile_obj = User.objects.filter(
            forget_password_token=token).first()
        context = {
            'profile_obj': profile_obj.id
        }
        return render(request, 'account/changepassword.html', context)

    def post(self, request, token):
        profile_obj = User.objects.filter(
            forget_password_token=token).first()
        context = {
            'profile_obj': profile_obj.id
        }
        new_password = request.POST.get('newpassword')
        confirm_password = request.POST.get('confirmpassword')
        user_id = request.POST.get('user_id')

        if user_id is None:
            messages.error(request, 'No user id found')
            return render(request, 'account/changepassword.html', context)

        if (len(new_password) < 8):
            messages.error(request, "password is short")
            return render(request, 'account/changepassword.html', context)
        else:
            if(checkpassword(new_password)==True):
                if new_password != confirm_password:
                    messages.error(request, "both password should be same")
                    return render(request, 'account/changepassword.html', context)

                user_obj = User.objects.get(id=user_id)
                user_obj.set_password(new_password)
                user_obj.save()
                messages.success(request,'password has been change')
                return redirect('customer_login')
            else:
                msg = checkpassword(new_password)
                messages.error(request,msg)
                return render(request, 'account/changepassword.html', context)
            
        