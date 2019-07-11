"""sysestoque URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include, url
from .views import RegisterView, CustomLoginView

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^rest-auth/login/', CustomLoginView.as_view()),
    url(r'^rest-auth/registration/', RegisterView.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^', include('product.urls')),
    url(r'^', include('category.urls')),
    url(r'^', include('client.urls')),
    url(r'^', include('client_address.urls')),
    url(r'^', include('seller.urls')),
    # url(r'^', include('order.urls')),
    # url(r'^', include('order_itens.urls')),
    url(r'^', include('stock.urls'))
]
