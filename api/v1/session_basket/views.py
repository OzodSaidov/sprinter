from pprint import pprint

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.models import Product
from .basket import Basket
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from .validation import SessionProductOrderValidation

class TemporaryBasketCreateApi(GenericAPIView):
    """ Temporarily create basket in session """

    permission_classes = [AllowAny, ]

    def get(self, request):
        product_id = request.data.get('product', 0)
        params = request.data.get('params', [])
        color_id = request.data.get('color', 0)
        quantity = request.data.get('quantity', 0)
        basket = Basket(request=request)
        product = Product.objects.filter(id=product_id, is_active=True)
        if product.exists():
            validator = SessionProductOrderValidation(product=product.last(), params=params, quantity=quantity,
                                                      color_id=color_id)
            validator.validate()
            basket.add(product=product.last(), params=params, quantity=quantity, color_id=color_id)
            return Response('Successfully added', status=200)
        else:
            return Response('Product not found')

