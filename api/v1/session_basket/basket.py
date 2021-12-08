from decimal import Decimal
from django.conf import settings
from core.models import Product, ProductParam

BASKET_SESSION_ID = {}


class Basket(object):
    def __init__(self, request):
        self.session = request.session.session_key
        if not BASKET_SESSION_ID.get(self.session):
            BASKET_SESSION_ID[self.session] = []
        user = BASKET_SESSION_ID.get(self.session)
        if user == '':
            basket = []
            BASKET_SESSION_ID[self.session] = basket
        basket = BASKET_SESSION_ID[self.session]
        self.basket = basket

    def add(self, product, params,  quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """

        product_order = dict(product_id=product.id, quantity=quantity, params=sorted(params), price=product.price)
        self.basket.append(product_order)
        BASKET_SESSION_ID[self.session] = self.basket

