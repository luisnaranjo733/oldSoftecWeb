from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'test': 'Hello, World!'
    }
    return render(request, 'softecApp/index.html', context)