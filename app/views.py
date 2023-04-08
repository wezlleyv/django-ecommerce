from django.shortcuts import render
from django.http import HttpResponseRedirect

from products.models import *

# Create your views here.
def index(request):
    Context = {}

    Context['product'] = Product.objects.all()
    
    return render(request, "index.html", Context)

def category(request, category):
    Context = {}
    Context['product'] = Product.objects.filter(tags__exact=category)

    return render(request, 'index.html', Context)