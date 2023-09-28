from django.urls import path,include
from productowner.views import profile 


urlpatterns = [
    path('productwonerprofile/<str:pk>',profile.ProductOwnerProfile.as_view(),name="pprofile"),

]