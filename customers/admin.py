from django.contrib import admin
from import_export import resources
from customers.models import Customer

# Register your models here.

admin.site.register(Customer)

class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer