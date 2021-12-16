import json
from pprint import pprint

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import JsonResponse
from core.models import Product, ProductColor, ProductParam
from sprinter_settings import settings
from .basket import Basket
from django.http import HttpResponse
from rest_framework.views import APIView
from django.core.exceptions import ValidationError

from .validation import SessionProductOrderValidation
from ..product.serializers import ProductRetrieveSerializer, ProductShortDetailSerializer, ColorSerializer, \
    ProductParamSerializer
from django.db.models import Sum

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
            if validator.validate():
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
            if validator.validate():
                basket.update(product=product.last(), params=params, color_id=color_id, quantity=quantity, id=id)
            return JsonResponse(basket.current_product, safe=False)
        else:
            return JsonResponse('Product not found', safe=False)


class TemporaryBasketListApi(APIView):
    """ List of products in session """

    permission_classes = [AllowAny, ]

    def get(self, request):
        basket = Basket(request=request).basket
        result = {}
        data = []
        total_price = 0
        for b in basket:
            product = Product.objects.filter(id=b.get('product_id', 0))
            color = ProductColor.objects.filter(id=b.get('color_id', 0))
            params = ProductParam.objects.filter(id__in=b.get('params', []))
            if product.exists() and color.exists():
                product = product.last()
                temp = {}
                url_scheme = '{}://{}{}{}'.format(request.scheme, request.get_host(),
                                                  settings.MEDIA_URL, color.last().images.last().image)
                temp['id'] = b.get('id')
                temp['product'] = ProductShortDetailSerializer(instance=product, many=False).data
                temp['color'] = dict(color=color.last().color, image=url_scheme)
                temp['quantity'] = b.get('quantity')
                temp['params'] = ProductParamSerializer(instance=params, many=True).data

                additional_price = product.prices.filter(
                    param__in=b.get('params')).aggregate(additional_price=Sum('price'))
                product_price = product.price
                if additional_price.get('additional_price'):
                    product_price += additional_price['additional_price']
                temp['product_price'] = product_price
                data.append(temp)
                total_price += product_price * temp['quantity']
        result['products'] = data
        result['total_price'] = total_price
        return JsonResponse(result, safe=False)


class TemporaryBasketDeleteApi(APIView):
    """ Delete products from session """

    permission_classes = [AllowAny, ]

    def post(self, request):
        id = request.data.get('id', 0)
        basket = Basket(request=request)
        basket.remove_(id=id)
        return HttpResponse(status=200)


class TemporaryBasketProductsCount(APIView):
    """ Get number of products in basket """

    permission_classes = [AllowAny, ]

    def get(self, request):
        basket = Basket(request=request)
        data = dict(count=len(basket.basket))
        return JsonResponse(data)

