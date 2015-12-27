from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^orders/createOrder$', views.createOrder, name='createOrder'),
    url(r'^orders/addToOrder$', views.addToOrder, name='addToOrder'),
]