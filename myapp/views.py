from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def elements(request):
    return render(request,'element.html')

def generic(request):
    return render(request,'generic.html')