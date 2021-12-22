import os

from clickuz import ClickUz


def click_url(order):
    return_url = os.getenv('WEB_URL')
    click = ClickUz.generate_url(order_id=order.id, amount=order.price, return_url=return_url)
    return click