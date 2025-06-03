from django.shortcuts import render
from django.views import View

# Create your views here.

def index(request):
    return render(request, 'ecommerce/index.html')

def product_list(request):
    return render(request, 'ecommerce/product-list.html')

class Index(View):
    template_name = 'ecommerce/index.html'

class ProductList(View):
    template_name = 'ecommerce/product-list.html'
