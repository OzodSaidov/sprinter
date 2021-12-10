import json
import pickle
from decimal import Decimal
from pprint import pprint

from django.conf import settings
from core.models import Product, ProductParam
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from django.core.cache import cache

# BASKET_SESSION_ID = {}
BASKET_SESSION_ID = "BASKET_SESSION_ID"


def get_or_create_session():
    """ Create dict in redis to keep session """

    if cache.get(BASKET_SESSION_ID):
        return cache.get(BASKET_SESSION_ID)
    else:
        cache.set(BASKET_SESSION_ID, {}, timeout=60*60)
        return cache.get(BASKET_SESSION_ID)


def update_session(session, basket):
    """ Update session """

    basket_session = cache.get(BASKET_SESSION_ID)
    basket_session[session] = basket
    cache.set(BASKET_SESSION_ID, basket_session, timeout=60*60)


def get_basket(session):
    basket_session = cache.get(BASKET_SESSION_ID)
    if basket_session.get(session) is not None:
        basket = basket_session.get(session)
    else:
        basket = []
        update_session(session=session, basket=basket)
    return basket


class Basket(object):
    def __init__(self, request):
        get_or_create_session()
        self.session = request.session.session_key
        self.basket = get_basket(self.session)
        self.current_product = None

    def add(self, product, quantity, color_id, params):
        """ Add product to basket """

        id = self.basket[-1]['id'] + 1 if len(self.basket) > 0 else 1
        product_order_dict = dict(id=id, product_id=product.id, quantity=quantity, color_id=color_id,
                                  params=sorted(params),
                                  price=product.price)

        old_product_order = self.check_product(product, color_id, params)
        if old_product_order is not None:
            product_order_dict['id'] = old_product_order['id']
            self.basket.remove(old_product_order)
        if product_order_dict['quantity'] > 0:
            self.basket.append(product_order_dict)
            self.current_product = product_order_dict
        update_session(session=self.session, basket=self.basket)


    def update(self, id, product, quantity, color_id, params):
        """ Update of product in basket """

        product_order_dict = dict(id=0, product_id=0, quantity=quantity, color_id=color_id,
                                  params=sorted(params),
                                  price=product.price)
        for product_order in self.basket:
            if product_order['id'] == id and quantity > 0:
                product_order_dict['id'] = product_order['id']
                product_order_dict['product_id'] = product_order['product_id']
                old_product_order = self.check_product(product, color_id, params)
                if old_product_order is not None:
                    product_order_dict['quantity'] += old_product_order['quantity']
                    self.basket.remove(old_product_order)
                if not product_order == old_product_order:
                    self.basket.remove(product_order)
                self.basket.append(product_order_dict)
                self.current_product = product_order_dict
        update_session(session=self.session, basket=self.basket)

    def remove_(self, id):
        """ Remove product from basket """

        for product_order in self.basket:
            if product_order['id'] == int(id):
                self.basket.remove(product_order)
        update_session(session=self.session, basket=self.basket)

    def check_product(self, product, color_id, params):
        """ Check is product with same properties exist in basket """

        order = None
        for product_order in self.basket:
            if product_order['product_id'] == product.id and product_order['color_id'] == color_id \
                    and product_order['params'] == sorted(params):
                order = product_order
        return order