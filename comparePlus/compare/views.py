from django.shortcuts import render
from .models import *
from django.http import HttpResponse                                                      

# Create your views here.

def index(request):
    items = Items.objects.all()
    ratings = []

    for i in items:
        print(i.image)

    def star(n):
        return n * "*"
    
    for i in items:
        ratings.append(star(i.rating))

    return render(request,'compare/index.html', {
        'items': items,
        'ratings': ratings,

    })

def item(request,item):
    
    itemInfo = Items.objects.filter(item = item)

    return render(request, "compare/item.html",{
        'item':itemInfo
    })

def sign(request):
    return render(request,'compare/sign.html')