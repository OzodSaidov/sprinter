from rest_framework import generics
from rest_framework.permissions import AllowAny
# from django.contrib.postgres.search import SearchVector, SearchQuery

from api.v1.product.serializers import ProductListSerializer
from api.v1.search.get_query import get_query
from core.models import Product


class SearchProductView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        lang = self.request.LANGUAGE_CODE.lower()
        q = self.request.query_params.get('q')
        products = Product.objects.none()
        if q:
            search_fields = [f'catalog__title_{lang}', 'brand__title', f'title_{lang}',
                             f'description_{lang}', 'price']
            query = get_query(q, search_fields)
            products = Product.objects.filter(query).order_by('price')
        return products
