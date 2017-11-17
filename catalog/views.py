# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Catalog, Product

#def product_list(request):
#    products =  Product.objects.filter(available=True)
#    return render(request,
#                    'catalog/index.html',
#                    {'products': products})

def index(request):
	main_categories = Catalog.objects.all()
	template = loader.get_template('catalog/index.html')
	context = {
	'main_categories' : main_categories,
	}
	return HttpResponse(template.render(context,request))
