from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request,'compare/index.html', {
        'stores': Stores.objects.all()
    })