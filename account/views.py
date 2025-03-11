from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def accHello(request, name):
    return HttpResponse('Hello, '+name+'!')

def addtwo(request, num1, num2):
    sum_result = int(num1) + int(num2)
    return HttpResponse('the sum of ' + str(num1) + ' + ' + str(num2) + ' = ' + str(sum_result))

def home_page(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

