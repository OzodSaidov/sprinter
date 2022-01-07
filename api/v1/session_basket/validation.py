from core.models import ProductGroup, Product

from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponse


class SessionProductOrderValidation:
    def __init__(self, product, params, quantity, color_id):
        self.product = product
        self.product_params = params
        self.quantity = quantity
        self.color_id = color_id

    def validate(self):
        # Call all validators
        self.validate_product_params()
        self.validate_color()
        self.validate_quantity()

        return True

    def validate_product_params(self):
        # Checking product params
        groups = ProductGroup.objects.filter(productparam__in=self.product_params)
        if self.product.params.filter(pk__in=self.product_params, is_important=False).exists():
            raise ValidationError('Cannot choose param which is not important')
        elif self.product.params.exclude(pk__in=self.product_params, is_important=True).exclude(group__in=groups).exists():
            raise ValidationError('Not all params were chosen', code='invalid')
        elif len(self.product_params) != self.product.params.filter(is_important=True).distinct('group').count():
            raise ValidationError('Cannot assign several params from the same group')

    def validate_quantity(self):
        # Checking quantity
        if self.product.available_quantity < self.quantity:
            raise ValidationError('No such quantity available')

    def validate_color(self):
        # Checking if this color exists
        if not self.product.colors.filter(id=self.color_id).exists():
            raise ValidationError("No such color found")