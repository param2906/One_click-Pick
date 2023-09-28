"""One_click_pick URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from authentication.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include("authentication.urls")),
    path('',include("products.urls")),
    path('productowner/',include("productowner.urls")),
    path('customer/',include("customer.urls")),
    path('accounts/', include('allauth.urls')),
    path('order/',include('order.urls')),
    # path('social-auth',include('social_django.urls',namespace='social'))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 