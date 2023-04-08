from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

# Create your views here.
def list_products(request):
    ProductsContext = {}
    ProductsContext['dataset'] = Product.objects.all()

    return HttpResponse(ProductsContext['dataset'].title)
