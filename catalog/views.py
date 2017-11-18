# -*- coding:utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Catalog, Product
#from .models import Category

#def product_list(request):
#    products =  Product.objects.filter(available=True)
#    return render(request,
#                    'catalog/index.html',
#                    {'products': products})

def index(request):
	main_categories = Catalog.objects.all()
	#some
	template = loader.get_template('catalog/index.html')
	context = {
	'main_categories' : main_categories,
#	'SOME SUBCATEGORY': SUBCATEGORY,
	}
	return HttpResponse(template.render(context,request))
