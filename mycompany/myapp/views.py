from django.shortcuts import render

# Create your views here. هنا احنا نبرمج 
# هنا وحدة المعالجة
# هنا الباكاند

from django.http import HttpResponse

def Message(request):
    return HttpResponse('Hello, Django!') # الحين ننشئ راوت

def Home(request):
    return HttpResponse('Hello, this is the home page') # الحين ننشئ راوت