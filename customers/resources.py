from import_export import resources
from .models import Customer

class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer
        fields = (
            'full_name',
            'email',
            'phone_number',
            'address',
            'joined',
        )