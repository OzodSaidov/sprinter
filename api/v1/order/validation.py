from core.models import ProductGroup

from django.core.exceptions import ValidationError


class ProductOrderValidation:
    def __init__(self, product_order, product, attrs):
        self.product_order = product_order
        self.product = product
        self.product_params = attrs.get('product_param', [])
        self.quantity = attrs.get('quantity', 0)

    def validate_product_params(self):
        # Checking product params
        product_params = [product_param.id for product_param in self.product_params]
        groups = ProductGroup.objects.filter(productparam__in=product_params)
        if self.product.params.filter(pk__in=product_params, is_important=False).exists():
            raise ValidationError('Cannot choose param which is not important')
        elif self.product.params.exclude(pk__in=product_params, is_important=True).exclude(group__in=groups).exists():
            raise ValidationError('Not all params were chosen')
        elif len(product_params) != self.product.params.filter(is_important=True).distinct('group').count():
            raise ValidationError('Cannot assign several params from the same group')

    def validate_quantity(self):
        # Checking quantity
        if self.product.available_quantity < self.quantity:
            raise ValidationError('No such quantity available')
