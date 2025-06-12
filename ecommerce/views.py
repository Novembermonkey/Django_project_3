from django.shortcuts import render
from .models import Product, Category, Comment
from django.views import View
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator


# Create your views here.


class Index(View):
    def get(self, request, category_slug=None):
        products = Product.objects.all()
        categories = Category.objects.all()

        paginator = Paginator(products, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'categories': categories,
            'page_obj': page_obj,
        }

        if category_slug:
            products = products.filter(category__slug=category_slug)
            return render(request, 'ecommerce/product-list.html', {'products': products})
        return render(request, 'ecommerce/index.html', context=context)


def product_list(request):
    return render(request, 'ecommerce/product-list.html', {'products': Product.objects.all()})

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


