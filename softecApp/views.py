from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import logout

def index(request):
    context = {
        'test': 'Hello, World!'
    }
    return render(request, 'softecApp/index.html', context)

def logOut(request):
    logout(request)
    return redirect('index')

def createOrder(request):
    if request.method == 'POST':
        return HttpResponse(str(request.POST))
    else:
        raise Http404

def addToOrder(request):
    return HttpResponse('adding to order')

