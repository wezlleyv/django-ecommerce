from django.shortcuts import render
from django.http import HttpResponseRedirect

from products.models import *

# Create your views here.
def index(request):
    Context = {}

    Context['dataset'] = Product.objects.all()
    
    return render(request, "index.html", Context)