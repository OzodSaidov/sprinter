import os

from clickuz import ClickUz
from common.static_data import PaymentType


def click_url(order):
    click_url = ClickUz.generate_url(order_id=order.id, amount=order.price, return_url='https://sprinter.uz/success-payment')
    url = dict(url=click_url, type=PaymentType.CLICK)
    return url