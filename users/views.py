from django.shortcuts import render
from django.views.generic import CreateView
from .models import CustomUser
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.urls import reverse_lazy

# Create your views here.

def login_page(request):
    return render(request, 'users/login.html')

class LoginUser(LoginView):
    authentication_form = LoginForm
    template_name = 'users/login.html'
    extra_context = {}

    def get_success_url(self):
        return reverse_lazy('ecommerce:index')



def register_page(request):
    return render(request, 'users/register.html')

class RegisterUser(CreateView):
    model = CustomUser
    template_name = 'users/register.html'
    fields = ('email', 'password', 'confirmed_password')

    def form_valid(self, form):
        if form.cd['password'] == form.cd['confirmed_password']:
            form.save()

def mail_confirmation(request):
    return render(request, 'users/confirm-mail.html')
