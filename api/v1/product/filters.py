from django_filters import rest_framework as rest_filter

from core.models import Product, Review, Comment


class ProductFilter(rest_filter.FilterSet):
    title = rest_filter.CharFilter(field_name='title')
    min_price = rest_filter.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = rest_filter.NumberFilter(field_name='price', lookup_expr='lte')
    is_new = rest_filter.BooleanFilter(field_name='is_new')
    is_stock = rest_filter.BooleanFilter(field_name='is_stock')
    catalog_id__in = rest_filter.filters.BaseInFilter(
        field_name='catalogs',
        lookup_expr='in'
    )

    class Meta:
        model = Product
        fields = {
            'brand_id': ['in'],
            # 'catalogs_id__in': [],
            'discount': ['isnull'],
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
