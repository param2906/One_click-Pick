from user.models import User
from django.shortcuts import redirect, render
from django.views import View
import uuid
from django.contrib import messages
from authentication.helpers import send_forget_password_email
class Forgetpassword(View):
    def get(self, request):
        return render(request, 'account/forgetpassword.html')

    def post(self, request):
        email = request.POST.get('email')

        if User.objects.filter(email=email).exists():
            user_object = User.objects.get(email=email)
            token = str(uuid.uuid4())
            # user = User.objects.get(name=user_object)

            user_object.forget_password_token = token
            # print(customer.forget_password_token)
            user_object.save()
            send_forget_password_email(user_object, token)
            messages.success(request, 'email has been sent')
            return redirect('forgetpassword')
            
        else:
            messages.error(request, 'User is not found')
            return redirect('forgetpassword')
        # token = str(uuid.uuid4())
        