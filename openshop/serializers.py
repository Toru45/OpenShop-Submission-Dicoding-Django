from rest_framework import serializers
from openshop.models import OpenShop

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenShop
        fields = [
            'id',
            'name',
            'sku',
            'description',
            'shop',
            'location',
            'price',
            'discount',
            'category',
            'stock',
            'is_available',
            'picture',
            'is_delete',
        ]