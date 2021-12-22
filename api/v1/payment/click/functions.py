import os

from clickuz import ClickUz
from common.static_data import PaymentType


def click_url(order):
    return_url = os.getenv('WEB_URL')
    click_url = ClickUz.generate_url(order_id=order.id, amount=order.price, return_url=return_url)
    url = dict(url=click_url, type=PaymentType.CLICK)
    return url