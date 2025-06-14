from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import LoginForm, RegisterForm
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
    form_class = RegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ecommerce:index')

def mail_confirmation(request):
    return render(request, 'users/confirm-mail.html')
