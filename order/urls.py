from django.urls import path
from order.views import checkout,order,ownersorder,payment,updatedetails,success
urlpatterns = [
    path('checkout/<str:pk>',checkout.Checkout.as_view(), name ='checkout'),
    path('order/<str:pk>',order.Orders.as_view(),name='order'),
    path('ownerorder/<str:pk>',ownersorder.Ownerorder.as_view(),name='ownerorder'),
    path('payment/<str:pk>',payment.Payment.as_view(),name = 'payment'),
    path('updatecheckout/<str:pk>',updatedetails.Updatedetails.as_view(), name='updatedetails'),
    path('success/<str:pk>',success.Success.as_view(),name = 'success')
]   