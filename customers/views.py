from django.shortcuts import render
from .models import Customer
from .admin import CustomerResource
from django.http import HttpResponse
from django.views.generic import ListView
from import_export.formats.base_formats import XLSX

# Create your views here.

# def customers_list(request):
#     customers = Customer.objects.all()
#     page_obj = pagination(request, customers, 1)
#
#     return render(request, 'customers/customers-list.html', {'page_obj': page_obj})

class CustomersList(ListView):
    model = Customer
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'
    paginate_by = 1



def customers_export(request):
    customers = Customer.objects.all()
    format = request.GET.get('format')
    resource = CustomerResource()
    dataset = resource.export(customers)

    if format == 'csv':
        file =  dataset.csv
        file_ext = 'csv'
    elif format == 'json':
        file = dataset.json
        file_ext = 'json'
    else:
        file_format = XLSX()
        file_ext = 'xlsx'
        file = file_format.export_data(dataset)
    response = HttpResponse(file)
    response['Content-Disposition'] = f'attachment; filename="customers.{file_ext}"'
    return response

