from django.urls import path
from ecommerce import views

app_name = 'ecommerce'

urlpatterns = [
            path('', views.index, name='index'),
            path('product-list/', views.product_list, name='product_list'),
]