from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from ecommerce.models import Product, Category


class ProductResource(resources.ModelResource):
    category = fields.Field(
        column_name='category',
        attribute='category',
        widget=ForeignKeyWidget(Category, 'id'),
    )

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'discount', 'amount', 'category',)