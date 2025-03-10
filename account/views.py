from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def accHello(request):
    return HttpResponse('Hello, in Account!')
