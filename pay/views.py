from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.
def order(request):
    return HttpResponse('order')
