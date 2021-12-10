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
        self.current_product = None

    def add(self, product, quantity, color_id, params):
        """
        Add product to basket
        """

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
        BASKET_SESSION_ID[self.session] = self.basket

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
                self.basket.remove(product_order)
                self.basket.append(product_order_dict)
                self.current_product = product_order_dict
        BASKET_SESSION_ID[self.session] = self.basket

    def remove_(self, id):
        """ Remove product from basket """

        for product_order in self.basket:
            if product_order['id'] == int(id):
                self.basket.remove(product_order)
        BASKET_SESSION_ID[self.session] = self.basket


    def check_product(self, product, color_id, params):
        """ Check is product with same properties exist in basket """

        order = None
        for product_order in self.basket:
            if product_order['product_id'] == product.id and product_order['color_id'] == color_id \
                    and product_order['params'] == sorted(params):
                order = product_order
        return order