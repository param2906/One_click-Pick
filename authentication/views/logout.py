from django.views import View
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import logout


class logoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('customer_login')