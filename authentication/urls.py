from django.contrib import admin
from django.urls import path,include
from authentication.views import register,login,logout,otp,resetpassword,changepassword,forgetpassword
from products.views import index

urlpatterns = [
    path('register/',register.Register.as_view(),name='customer_register'),
    path('login/', login.Login.as_view(), name='customer_login'),
    path('logout/',logout.logoutUser.as_view(),name='logout'),
    path('index/',index.Index.as_view(),name='index'),
    path('productAdminRegister/',register.ProductadminRegister.as_view(),name='productAdminRegister'),
    path('registrationOtp/',otp.Otp.as_view(),name='registrationOtp'),
    path('resetpassword/', resetpassword.Resetpassword.as_view(), name='resetpassword'),
    path('changepassword/<token>/',changepassword.Changepassword.as_view(),name='changepassword'),
    path('fogetpassword/',forgetpassword.Forgetpassword.as_view(),name='forgetpassword'),

]