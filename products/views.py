from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    # return HttpResponse("Hello Django")
    products = Product.objects.all()
    return render(request, 'index.html', {
        'products' : products
    })


def new(request):
    return HttpResponse("This is a new product page")

