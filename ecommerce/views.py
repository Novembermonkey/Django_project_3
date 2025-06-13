from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .models import Product, Category, Comment
from django.views import View
from django.views.generic import DetailView, CreateView, ListView
from django.urls import reverse_lazy
from .utils import search


# Create your views here

class Index(ListView):
    model = Product
    template_name = 'ecommerce/index.html'
    context_object_name = 'products'
    paginate_by = 1

    def get_queryset(self):
        products = Product.objects.all()

        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            products = products.filter(category__slug=category_slug)

        products = search(self.request, products)
        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.get_queryset()

        context['products'] = products
        context['categories'] = Category.objects.all()

        if self.kwargs.get('category_slug'):
            self.template_name = 'ecommerce/product-list.html'

        return context


class ProductList(ListView):
    model = Product
    template_name = 'ecommerce/product-list.html'
    context_object_name = 'products'
    paginate_by = 1


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


