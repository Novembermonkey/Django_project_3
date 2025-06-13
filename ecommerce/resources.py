from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from ecommerce.models import Product


class ProductResource(resources.ModelResource):
    category = fields.Field(
        column_name='category',
        attribute='category',
        widget=ForeignKeyWidget(Product, 'title'),
    )

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'discount', 'amount', 'category',)