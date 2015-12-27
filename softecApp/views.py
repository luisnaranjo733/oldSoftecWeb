from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from softecApp.models import Staff, Restaurant, Customer, Order, Product, OrderProduct

def index(request):
    context = {
        'test': 'Hello, World!'
    }
    return render(request, 'softecApp/index.html', context)

def logOut(request):
    logout(request)
    return redirect('index')

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

