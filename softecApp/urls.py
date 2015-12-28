from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout$', views.logOut, name='logOut'),
    url(r'^supplies$', views.viewOrders, name='viewOrders'),
    url(r'^orders/createOrder$', views.createOrder, name='createOrder'),
    url(r'^orders/addToOrder$', views.addToOrder, name='addToOrder'),
]