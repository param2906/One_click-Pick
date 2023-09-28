from django.urls import path,include
from products.views import index,createproduct,products,updateproduct,deleteproduct,shop,details,category
from authentication.views import logout
urlpatterns = [
    path('',index.Index.as_view(),name ='index'),
    path('createproduct/',createproduct.CreateProduct.as_view(), name='createproduct'),
    path('logout/',logout.logoutUser.as_view(),name='logout'),  
    # path('login/', login.Login.as_view(), name='customer_login'),
    path('products/',products.UserProducts.as_view(),name='products'),
    path('updateproduct/<str:pk>',updateproduct.UpdateProduct.as_view(),name='updateproduct'),
    path('deleteproduct/<str:pk>',deleteproduct.DeleteProduct.as_view(),name='deleteproduct'),
    path('shop/',shop.Shop.as_view(),name ='shop'),
    path('detail/<str:pk>',details.Details.as_view(),name='detail'),
    path('category/<str:pk>/',category.Category.as_view(),name='category'),
]
