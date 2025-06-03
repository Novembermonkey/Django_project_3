from django.shortcuts import render
from .models import Product, Category
from django.views import View

# Create your views here.

def index(request):

    context = {
            'categories': Category.objects.all(),
            'products': Product.objects.all(),
    }

    return render(request, 'ecommerce/index.html', context=context)

def product_list(request):
    return render(request, 'ecommerce/product-list.html')

class Index(View):
    def get(self, request):
        context = {
            'categories': Category.objects.all(),
            'products': Product.objects.all(),
        }
        return render(request, 'ecommerce/index.html', context=context)
