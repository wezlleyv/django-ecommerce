from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,  HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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

def myProducts(request):
    context = {}
    context['product'] = Product.objects.filter(owner__exact=request.user.username)
    context['myProduct'] = True

    return render(request, 'index.html', context)

def searchDB(request):
    if request.method == 'POST':
        obj = request.POST.get("search")
        
        context = {}
        context['product'] = Product.objects.filter(title__contains=obj)

        return render(request, 'index.html', context)


def accountFormRegister(request):
    form = UserCreationForm()

    context = {'form': form}

    return render(request, "accountReg.html", context)



def regAccount(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return HttpResponseRedirect('/login')