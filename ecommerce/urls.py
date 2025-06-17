from django.urls import path
from ecommerce import views

app_name = 'ecommerce'

urlpatterns = [
        path('', views.Index.as_view(), name='index'),
        path('product-list/', views.ProductList.as_view(), name='product_list'),
        path('category/<slug:category_slug>', views.Index.as_view(), name = 'products_by_category'),
        path('product/detail/<int:pk>', views.ProductDetail.as_view(), name = 'product_detail'),
        path('product/detail/<int:pk>/comment/create', views.CommentCreate.as_view(), name = 'create_comment'),

        #email
        path('send-email/', views.send_email, name = 'send_email'),
]