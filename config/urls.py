"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from baton.autodiscover import admin
from django.urls import path, include
from django.conf.urls.static import static
from config import settings
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('ecommerce:index')),
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('ecommerce/', include('ecommerce.urls', namespace='ecommerce')),
    path('users/', include('users.urls', namespace='users')),
    path('customers/', include('customers.urls', namespace='customers')),

    path('auth/', include('social_django.urls', namespace='social')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
