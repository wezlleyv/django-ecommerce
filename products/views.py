from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate

from .models import Product

# Create your views here.
def createProduct(request):
    if request.method == 'POST':
            product = Product()
            product.title = request.POST.get('title')
            product.description = request.POST.get('description')
            product.price = request.POST.get('price')
            product.quantity = request.POST.get('quantity')
            product.tags = request.POST.get('tags')
            
            if len(request.FILES) != 0:
                print("a imagem foi")
                product.image = request.FILES['image']

            print(len(request.FILES))

            product.owner = request.user.username

            product.save()
            return redirect("home")
    if request.user.is_authenticated:
        pass
    else:
        return redirect("login")
    return render(request, "createProduct.html")