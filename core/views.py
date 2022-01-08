from django.shortcuts import render

from clickuz import ClickUz
from clickuz.views import ClickUzMerchantAPIView
from common.static_data import OrderStatus, PaymentStatus, PaymentType
from paycomuz import Paycom
from paycomuz.views import MerchantAPIView as PaymeMerchantAPIView
from core.models.order import Order
from loguru import logger

""" Payme """


class PaymeCheckOrder(Paycom):
    def check_order(self, amount, account, *args, **kwargs):
        try:
            order_id = str(account['order_id'])
            order = Order.objects.filter(id=int(order_id), order_status=OrderStatus.OPENED).first()
            logger.warning(f"Order id: {order_id}")
            if not order:
                logger.warning(f"Order not found: {order_id}")
                return self.ORDER_NOT_FOUND
            if not order.payment_type != PaymentType.PAYME:
                logger.warning(f'Order payment type is not payme: {order_id}')
                return self.ORDER_NOT_FOUND
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
    VALIDATE_CLASS = PaymeCheckOrder


#Click
class ClickCheckOrder(ClickUz):
    def check_order(self, order_id: str, amount: str):
        try:
            if not str(amount).isnumeric():
                return self.INVALID_AMOUNT
            order = Order.objects.filter(id=order_id, payment_status=PaymentStatus.WAITING).first()
            if not order:
                return self.ORDER_NOT_FOUND
            if not order.payment_type != PaymentType.CLICK:
                logger.warning(f'Order payment type is not click: {order_id}')
                return self.ORDER_NOT_FOUND
            if order.price != float(amount):
                return self.INVALID_AMOUNT
            return self.ORDER_FOUND
        except Exception as e:
            print('ClickError:', e)
            return self.ORDER_NOT_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        order = Order.objects.filter(id=order_id)
        if order.exists():
            order = order.last()
            order.payment_status = PaymentStatus.PAYED
            order.save()
        try:
            # amocrm_object.create_lead_note(order.lead_id, note_type="invoice_paid", params=new_note)
            print('CLICK SUCCESSFUL: Note:', order.user.user_id, 'state: ', order.state)
        except Exception as e:
            print(f'ClickError:', e)


class TestViewClickUz(ClickUzMerchantAPIView):
    VALIDATE_CLASS = ClickCheckOrder