from rest_framework import serializers
from openshop.models import OpenShop
from rest_framework.reverse import reverse

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    _links = serializers.SerializerMethodField()
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
            '_links',
        ]
    def get__links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self",
                "href": reverse('product-list', request=request),
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('product-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('product-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "PUT",
                "types": ["application/json"]
            }

        ]