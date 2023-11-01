from import_export import resources
from .models import Products,Category

class ProductResource(resources.ModelResource):
    class Meta:
        model = Products

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category