"""softecProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from softecApp import views

urlpatterns = [
    # url(r'^', include('softecApp.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^logout$', views.logOut, name='logOut'),
    url(r'^products$', views.listProducts, name='listProducts'),
    url(r'^products/(?P<product_id>[0-9]+)/$', views.showProduct, name='showProduct'),
    url(r'^orders/createOrder$', views.createOrder, name='createOrder'),
    url(r'^orders/addToOrder$', views.addToOrder, name='addToOrder'),
    url(r'^admin/', admin.site.urls, name="admin"),
]
