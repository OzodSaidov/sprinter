from rest_framework.views import APIView
from paycomuz.methods_subscribe_api import PayComResponse
from django.core.exceptions import ValidationError
from core.models.order import Order
from common.static_data import PaymentStatus, OrderStatus
from django.http import JsonResponse


class PayOrderWithPaymeApi(APIView):
    """ Make payment via payme """

    def post(self, request):
        order_id = request.data.get('order_id', None)
        order = Order.objects.filter(id=order_id, payment_status=PaymentStatus.WAITING,
                                      order_status=OrderStatus.OPENED)
        if not order_id:
            return JsonResponse(dict(order_id='Order is not given'))
        elif not order.exists():
            return JsonResponse(dict(order='Order does not exist'))
        else:
            order = order.last()
            paycom_response = PayComResponse()
            url = paycom_response.create_initialization(amount=order.price * 100, order_id=order.id,
                                                        return_url='https://sprinter.uz/')
            data = dict(payment_url=url)
            return JsonResponse(data)