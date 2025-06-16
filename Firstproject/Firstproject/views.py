from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world, This is home page")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Hello world, This is about page")

def contact(request):
    return HttpResponse("Hello world, thi is Contact page")