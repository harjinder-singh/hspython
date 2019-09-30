from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "home.html", {'page':'second'})

def add(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    res = num1+num2 
    return render(request, "result.html", {'result':res})
