from re import search

from django.shortcuts import render
from .models import Product, Category, Comment
from django.views import View
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from .utils import pagination, search


# Create your views here.


class Index(View):
    def get(self, request, category_slug=None):
        products = Product.objects.all()
        categories = Category.objects.all()

        products = search(request, products)

        page_obj = pagination(request, products, 1)

        context = {
            'categories': categories,
            'page_obj': page_obj,
        }

        if category_slug:
            products = products.filter(category__slug=category_slug)
            products = search(request, products)
            page_obj = pagination(request, products, 1)
            return render(request, 'ecommerce/product-list.html', {'page_obj': page_obj, })
        return render(request, 'ecommerce/index.html', context=context)


def product_list(request):
    products = Product.objects.all()
    page_obj = pagination(request, products, 1)
    return render(request, 'ecommerce/product-list.html', {'page_obj': page_obj})


class ProductDetail(DetailView):
    model = Product
    template_name = 'ecommerce/product-details.html'
    pk_url_kwarg = 'pk'


class CommentCreate(CreateView):
    model = Comment
    template_name = 'ecommerce/product-details.html'
    fields = ('name', 'email', 'content', 'rating')

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        product = Product.objects.get(pk=pk)

        form.instance.product = product

        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse_lazy('ecommerce:product_detail', kwargs={'pk': pk})


