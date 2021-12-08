from pprint import pprint

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.models import Product
from .basket import Basket
from django.http import HttpResponse


class TemporaryBasketCreateApi(GenericAPIView):
    """ Temporarily create basket in session """

    permission_classes = [AllowAny, ]

    def get(self, request):
        product_id = request.data.get('product', 0)
        params = request.data.get('params', [])
        basket = Basket(request=request)
        product = Product.objects.filter(id=product_id, is_active=True)
        if product.exists():
            print(product.last().params.filter(id__in=params, is_important=True).count())
            if product.last().params.filter(id__in=params, is_important=True).count() != len(params):
                return Response('No param found')
            basket.add(product=product.last(), params=params, update_quantity=False)
            pprint(basket.basket)
            return Response('Successfully added', status=200)
        else:
            return Response('Product not found')

