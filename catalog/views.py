from django.shortcuts import render
from .models import Catalog, Product

def product_list(request):
    products =  Product.objects.filter(available=True)
    return render(request,
                    'catalog/base.html',
                    {'products': products})