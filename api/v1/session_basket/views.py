import json
from pprint import pprint

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import JsonResponse
from core.models import Product
from .basket import Basket
from django.http import HttpResponse
from rest_framework.views import APIView
from django.core.exceptions import ValidationError

from .validation import SessionProductOrderValidation


class TemporaryBasketCreateApi(APIView):
    """ Temporarily create basket in session """

    permission_classes = [AllowAny, ]

    def post(self, request):
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
            basket.add(product=product.last(), quantity=quantity,color_id=color_id, params=params)
            return JsonResponse(basket.current_product, safe=False)
        else:
            return Response('Product not found')


class TemporaryBasketUpdateApi(APIView):
    """ Update product in session """

    permission_classes = [AllowAny, ]

    def post(self, request):
        id = request.data.get('id', 0)
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
            basket.update(product=product.last(), params=params, color_id=color_id, quantity=quantity, id=id)
            return JsonResponse(basket.current_product, safe=False)
        else:
            return Response('Product not found')


class TemporaryBasketListApi(APIView):
    """ List of products in session """

    permission_classes = [AllowAny, ]

    def get(self, request):
        basket = Basket(request=request)
        return JsonResponse(basket.basket, safe=False)


class TemporaryBasketDeleteApi(APIView):
    """ Delete products from session """

    permission_classes = [AllowAny, ]
    http_method_names = ['POST',]

    def post(self, request):
        id = request.data.get('id', 0)
        basket = Basket(request=request)
        basket.remove_(id=id)
        return HttpResponse(status=200)