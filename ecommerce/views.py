from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'ecommerce/index.html')

def product_list(request):
    return render(request, 'ecommerce/product-list.html')
