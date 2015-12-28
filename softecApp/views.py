from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from softecApp.models import *

def index(request):
    context = {}
    return render(request, 'index.html', context)

def logOut(request):
    logout(request)
    return redirect('index')

def listProducts(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'orders.html', context)

def showProduct(request, product_id):
    context = {
        'product': get_object_or_404(Product, pk=product_id)
    }
    return render(request, 'product.html', context)

@login_required
def createOrder(request):
    if request.method == 'POST':
        customer = Customer.objects.filter(user=request.user).first()
        order = Order()
        order.customer = customer
        order.save()
        return JsonResponse({
                'id': order.id,
                'customer': {
                    'username': order.customer.user.username,
                    'id': order.customer.user.id
                }
            })
    else:
        raise Http404

@login_required
def addToOrder(request):
    return HttpResponse('adding to order')

