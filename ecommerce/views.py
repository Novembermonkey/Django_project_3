from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import EmailForm
from .models import Product, Category, Comment
from django.views.generic import DetailView, CreateView, ListView
from django.urls import reverse_lazy
from .utils import search
from config.settings import DEFAULT_FROM_EMAIL
from django.db.models import Avg
from django.db.models.functions import Round


# Create your views here

class Index(ListView):
    model = Product
    template_name = 'ecommerce/index.html'
    context_object_name = 'products'
    paginate_by = 1

    def get_queryset(self):
        products = Product.objects.annotate(avg_rating=Round(Avg('comments__rating'), precision=2))

        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            products = products.filter(category__slug=category_slug)

        products = search(self.request, products)
        return products.order_by('-avg_rating')

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
    paginate_by = 3

    def get_queryset(self):
        products = Product.objects.annotate(avg_rating=Round(Avg('comments__rating'), precision=2))
        return products.order_by('-avg_rating')


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



def send_email(request):
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            receivers = form.cleaned_data['receivers'].split(",")
            print(receivers)

            send_mail(subject=subject, message=message, from_email=DEFAULT_FROM_EMAIL, recipient_list=receivers)

            return redirect('ecommerce:index')

    return render(request, 'ecommerce/email.html', {'form': form})



# Product.objects.all().annotate(avg_rating=Round(Avg('comments__rating'), precision=2))
