from django.shortcuts import render
from django.http import HttpResponse, Http404

def index(request):
    context = {
        'test': 'Hello, World!'
    }
    return render(request, 'softecApp/index.html', context)

def createOrder(request):
    if request.method == 'POST':
        return HttpResponse(str(request.POST))
    else:
        raise Http404

def addToOrder(request):
    return HttpResponse('adding to order')