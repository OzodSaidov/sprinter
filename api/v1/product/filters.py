from django_filters import rest_framework as rest_filter

from core.models import Product, Review


class ProductFilter(rest_filter.FilterSet):
    min_price = rest_filter.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = rest_filter.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = {
            'brand_id': ['in'],
            'catalog_id': ['in'],
            'discount': ['isnull'],
            'status': ['iexact']
        }


class ReviewFilter(rest_filter.FilterSet):
    class Meta:
        model = Review
        fields = [
            'product_id'
        ]
