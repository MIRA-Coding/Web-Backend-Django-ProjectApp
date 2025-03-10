from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcomeHr(request):
    return HttpResponse('Hello, in Hr!') # الحين ننشئ راوت