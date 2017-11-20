from django.shortcuts import render
from .models import Catalog, Product

def product_list(request):
    products =  Product.objects.filter(available=True)
    catalogs = Catalog.objects.all()
    return render(request,
                    'catalog/list.html',
                    {'products': products,
                     'catalogs':catalogs})