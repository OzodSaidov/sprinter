from django_filters import rest_framework as rest_filter

from core.models import Product


class ProductFilter(rest_filter.FilterSet):
    min_price = rest_filter.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = rest_filter.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = {
            'brand_id': ['in'],
            'catalog_id': ['in'],
        }
