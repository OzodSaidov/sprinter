from rest_framework.views import APIView

from api.v1.payment.payme.functions import payme_url
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
            url = payme_url(order=order)
            data = dict(payment_url=url)
            return JsonResponse(data)