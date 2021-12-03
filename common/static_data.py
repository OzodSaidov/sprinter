from django.db.models import TextChoices


class PaymentType(TextChoices):
    CASH = 'Cash', 'Cash'
    CLICK = 'Click', 'Click'
    PAYME = 'Payme', 'Payme'


class OrderStatus(TextChoices):
    OPENED = 'Opened', 'Opened'
    ORDERED = 'Ordered', 'Ordered'
    APPROVED = 'Approved', 'Approved'
    DECLINED = 'Declined', 'Declined'
    CANCELLED = 'Cancelled', 'Cancelled'
    DELIVERING = 'Delivering', 'Delivering'
    COMPLETED = 'Completed', 'Completed'


class PaymentStatus(TextChoices):
    WAITING = 'Waiting', 'Waiting'
    PAYED = 'Payed', 'Payed'
    FAILURE = 'Failure', 'Failure'


class UserRoles(TextChoices):
    ADMIN = 'Admin'
    MODERATOR = 'Moderator'
    USER = 'User'


# class Quality(TextChoices):
#     PRICE = 'Price', 'Price'
#     RESPONSIVENESS = 'Responsiveness', 'Responsiveness'
#     COLOR = 'Color', 'Color'
#     DELIVERY_SPEED = 'Delivery speed', 'Delivery speed'
#     QUALITY = 'Quality', 'Quality'
