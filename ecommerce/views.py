from django.shortcuts import render
from .models import Product, Category
from django.views import View
from django.views.generic import DetailView

# Create your views here.


class Index(View):
    def get(self, request, category_slug=None):
        products = Product.objects.all()
        categories = Category.objects.all()

        context = {
            'categories': categories,
            'products': products,
        }

        if category_slug:
            products = products.filter(category__slug=category_slug)
            return render(request, 'ecommerce/product-list.html', {'products': products})
        return render(request, 'ecommerce/index.html', context=context)


def product_list(request):
    return render(request, 'ecommerce/product-list.html', {'products': Product.objects.all()})