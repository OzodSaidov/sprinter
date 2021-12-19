from common.static_data import PaymentType
from paycomuz import PayComResponse


def payme_url(order):
    paycom_response = PayComResponse()
    payme_url = paycom_response.create_initialization(amount=order.price * 100, order_id=str(order.id),
                                                      return_url='https://sprinter.uz/')
    url = dict(url=payme_url, type=PaymentType.PAYME)
    return url