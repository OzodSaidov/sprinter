from pprint import pprint

from api.v1.product.serializers import ProductShortDetailSerializer, ProductParamSerializer
from core.models import Product, ProductColor, ProductParam
from sprinter_settings import settings
from user.redis import get_or_create_session, get_basket, update_session
from django.db.models import Sum
from ipware import get_client_ip


class Basket(object):
    def __init__(self, request):
        get_or_create_session()
        self.request = request
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
                    # product_order_dict['quantity'] = old_product_order['quantity']
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

    def to_representation(self):
        result = {}
        data = []
        total_price = 0
        basket = sorted(self.basket, key=lambda b: b['id'])
        for b in basket:
            product = Product.objects.filter(id=b.get('product_id', 0))
            color = ProductColor.objects.filter(id=b.get('color_id', 0))
            params = ProductParam.objects.filter(id__in=b.get('params', []))
            if product.exists() and color.exists():
                product = product.last()
                temp = {}
                try:
                    url_scheme = '{}://{}{}{}'.format(self.request.scheme, self.request.get_host(),
                                                  settings.MEDIA_URL, color.last().images.last().image)
                except:
                    url_scheme = None
                temp['id'] = b.get('id')
                temp['product_id'] = product.id
                temp['product'] = ProductShortDetailSerializer(instance=product, many=False).data
                temp['color'] = dict(id=color.last().id, color=color.last().color, image=url_scheme)
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
        return result