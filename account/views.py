from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    return render(request, 'index.html' )

# def accoHello(request, name):
#     return render(request, 'index.html' )

def about(request):
    return render(request, 'about.html')


def addtwo(request, num1, num2):
    sum_result = int(num1) + int(num2)
    return render(request, 'the sum of ' + str(num1) + ' + ' + str(num2) + ' = ' + str(sum_result))

# def home_page(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render({}, request))


def home_page(request):
    return render(request, 'home.html')
