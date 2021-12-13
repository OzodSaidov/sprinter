from django.shortcuts import render

from common.static_data import OrderStatus, PaymentStatus, PaymentType
from paycomuz import Paycom
from paycomuz.views import MerchantAPIView as PaymeMerchantAPIView
from core.models.order import Order
from loguru import logger

""" Payme """


class CheckOrder(Paycom):
    def check_order(self, amount, account, *args, **kwargs):
        try:
            order_id = str(account['order_id'])
            order = Order.objects.filter(id=int(order_id), order_status=OrderStatus.APPROVED).first()
            logger.warning(f"Order id: {order_id}")
            if not order:
                logger.warning(f"Order not found: {order_id}")
                return self.ORDER_NOT_FOUND
            if not order.payment_type != PaymentType.PAYME:
                logger.warning(f'Order payment type is not payme: {order_id}')
            if order.payment_status != PaymentStatus.WAITING:
                logger.warning(f"Order state not waiting: {order_id}")
                return self.ORDER_NOT_FOUND
            if not str(amount).isnumeric():
                return self.INVALID_AMOUNT
            if 100 * order.price != amount:
                return self.INVALID_AMOUNT
            return self.ORDER_FOUND
        except Exception as e:
            logger.error(f'PaycomError: {e}')
            return self.ORDER_NOT_FOUND

    def successfully_payment(self, account, transaction, *args, **kwargs):
        try:
            order = Order.objects.filter(id=int(transaction.order_key)).first()
            if order:
                order.payment_status = PaymentStatus.PAYED
                order.save()
                # logger.success('PAYME SUCCESSFUL: User:', order.user.id, 'Payment status: ', order.payment_status)
                print('PAYME SUCCESSFUL: User:', order.user.id, 'Payment status: ', order.payment_status)
        except Exception as e:
            logger.error(f'PaycomError: {e}')

    def cancel_payment(self, account, transaction, *args, **kwargs):
        print(account)


class TestViewPaycom(PaymeMerchantAPIView):
    VALIDATE_CLASS = CheckOrder