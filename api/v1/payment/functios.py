from api.v1.payment.payme.functions import payme_url
from clickuz import ClickUz
from common.static_data import PaymentType
from api.v1.payment.click.functions import click_url


def payment_urls(order):
    url = {}
    payme = payme_url(order=order)
    click = click_url(order=order)
    url['payme'] = payme
    url['click'] = click

    return url
