from django.http import HttpResponse
from django.shortcuts import render

def navbar(request):
    context = {}
    # context['hello'] = 'hello world!'
    # return HttpResponse("Hello world!")
    return render(request, 'base.html', context)

def home(request):
    return render(request, 'home.html')

def visual(request):
    return render(request, 'visual.html')

def about(request):
    return render(request, 'about.html')