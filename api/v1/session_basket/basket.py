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
            BASKET_SESSION_ID[self.session] = []
        basket = BASKET_SESSION_ID[self.session]
        self.basket = basket

    def add(self, product, params, color_id, quantity):
        """
        Добавить продукт в корзину или обновить его количество.
        """

        id = self.basket[-1]['id'] + 1 if len(self.basket) > 0 else 1
        product_order_dict = dict(id=id, product_id=product.id, quantity=quantity, color_id=color_id,
                                  params=sorted(params),
                                  price=product.price)

        for product_order in self.basket:
            if product_order['product_id'] == product.id and product_order['color_id'] == color_id \
                    and product_order['params'] == sorted(params):
                product_order_dict['id'] = product_order['id']
                self.basket.remove(product_order)
        if product_order_dict['quantity'] > 0:
            self.basket.append(product_order_dict)
        BASKET_SESSION_ID[self.session] = self.basket
