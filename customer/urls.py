from django.urls import path,include
from customer.views import profile,showcart,deletecartitem


urlpatterns = [
    path('customer/<str:pk>/',profile.CustomerProfile.as_view(),name="cprofile"),
    path('cart/<str:pk>/',showcart.ShowCart.as_view(),name='showcart'),
    path('deletecartitem/<str:pk>',deletecartitem.Deletecartitem.as_view(),name='deletecartitem'),
]