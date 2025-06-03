from django.urls import path
from ecommerce import views

app_name = 'ecommerce'

urlpatterns = [
            path('', views.Index.as_view(), name='index'),
            path('product-list/', views.product_list, name='product_list'),
            path('category/<slug:category_slug>', views.Index.as_view(), name = 'products_by_category'),
]