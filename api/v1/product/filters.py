from django_filters import rest_framework as rest_filter

from core.models import Product, Review, Comment, Catalog


class ProductFilter(rest_filter.FilterSet):
    title = rest_filter.CharFilter(field_name='title')
    min_price = rest_filter.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = rest_filter.NumberFilter(field_name='price', lookup_expr='lte')
    is_new = rest_filter.BooleanFilter(field_name='is_new')
    is_stock = rest_filter.BooleanFilter(field_name='is_stock')
    catalog_id__in = rest_filter.filters.BaseInFilter(
        field_name='catalogs',
        # lookup_expr='in',
        method="get_catalog"
    )

    def get_catalog(self, queryset, name, values):
        catalogs = Catalog.objects.filter(id__in=values)
        catalogs = Catalog.objects.get_queryset_descendants(catalogs, include_self=True)
        queryset = Product.objects.filter(catalogs__in=catalogs)

        return queryset

    class Meta:
        model = Product
        fields = {
            'brand_id': ['in'],
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
