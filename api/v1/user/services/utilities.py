from core.models import Basket, ProductOrder, Product, ProductColor
from user.redis import get_basket, delete_basket
from django.db import transaction
import loguru


@transaction.atomic
def check_session_basket(user, request):
    """ Is user is registered and there is a basket in session, create basket for user """

    try:
        basket = get_basket(session=request.session.session_key)
        if len(basket) > 0:
            active_basket = user.basket.filter(is_active=True)
            if active_basket.exists():
                active_basket.last().delete()
            new_basket = Basket.objects.create(user=user)
            for product in basket:
                product_ = Product.objects.get(id=product['product_id'])
                color_ = ProductColor.objects.get(id=product['color_id'])
                product_order = ProductOrder.objects.create(
                    user=user,
                    product=product_,
                    quantity=product['quantity'],
                    color=color_)
                product_order.product_param.add(*product['params'])
                new_basket.products.add(product_order)
            delete_basket(request.session.session_key)
    except Exception as e:
        loguru.logger.error(e)
