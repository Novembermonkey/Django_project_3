from django.urls import path
from customers import views

app_name = 'customers'

urlpatterns = [
    path('', views.CustomersList.as_view(), name='customers_list'),
    path('export/', views.customers_export, name='customers_export'),
]