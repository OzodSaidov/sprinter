from api.v1.payment.payme.functions import payme_url
from common.static_data import PaymentType


def payment_urls(order):
    url = {}
    payme = payme_url(order=order)
    click = dict(url='click test url', type=PaymentType.CLICK)
    url['payme'] = payme
    url['click'] = click

    return url