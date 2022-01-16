from django.db.models import TextChoices


class PaymentType(TextChoices):
    CASH = 'Cash', 'Cash'
    CLICK = 'Click', 'Click'
    PAYME = 'Payme', 'Payme'


class OrderStatus(TextChoices):
    OPENED = 'Opened', 'Opened'
    CANCELLED = 'Cancelled', 'Cancelled'
    IN_PROCESS = 'In process', 'In process'
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


class ProductStatus(TextChoices):
    IN_STOCK = 1, "Есть в наличии"
    NON_STOCK = 2, "Нет в наличии"
    SOON = 3, "Скоро"

# class Quality(TextChoices):
#     PRICE = 'Price', 'Price'
#     RESPONSIVENESS = 'Responsiveness', 'Responsiveness'
#     COLOR = 'Color', 'Color'
#     DELIVERY_SPEED = 'Delivery speed', 'Delivery speed'
#     QUALITY = 'Quality', 'Quality'
