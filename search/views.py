from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.serializers import ModelSerializer

from .models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
