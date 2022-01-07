from django_filters import rest_framework as rest_filter

from core.models import Product, Review, Comment


class ProductFilter(rest_filter.FilterSet):
    min_price = rest_filter.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = rest_filter.NumberFilter(field_name='price', lookup_expr='lte')
    is_new = rest_filter.BooleanFilter(field_name='is_new')
    is_stock = rest_filter.BooleanFilter(field_name='is_stock')

    class Meta:
        model = Product
        fields = {
            'brand_id': ['in'],
            'catalog_id': ['in'],
            'discount': ['isnull']
        }


class ReviewFilter(rest_filter.FilterSet):
    class Meta:
        model = Review
        fields = [
            'product_id'
        ]


class CommentFilter(rest_filter.FilterSet):
    product_id = rest_filter.NumberFilter(field_name='product')

    class Meta:
        model = Comment
        fields = []
