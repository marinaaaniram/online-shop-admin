from rest_framework import viewsets
from products.models import Product
from products.serealizer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ('get',)