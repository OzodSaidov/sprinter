from core.models import ProductGroup

from django.core.exceptions import ValidationError


class ProductOrderValidation:
    def __init__(self, product, attrs):
        self.product = product
        self.product_params = attrs.get('product_param', [])
        self.quantity = attrs.get('quantity', 0)
        self.user = attrs.get('user')
        self.color = attrs.get('color')

        # Call all validators
        self.validate_product_params()
        self.validate_quantity()
        self.validate_quantity_for_existing_product()

    def validate_product_params(self):
        # Checking product params
        product_params = [product_param.id for product_param in self.product_params]
        groups = ProductGroup.objects.filter(productparam__in=product_params)
        if self.product.params.filter(pk__in=product_params, is_important=False).exists():
            raise ValidationError(dict(validation_error='Cannot choose param which is not important'))
        elif self.product.params.exclude(pk__in=product_params, is_important=True).exclude(group__in=groups).exists():
            raise ValidationError(dict(validation_error='Not all params were chosen'))
        elif len(product_params) != self.product.params.filter(is_important=True).distinct('group').count():
            raise ValidationError(dict(validation_error='Cannot assign several params from the same group'))

    def validate_quantity(self):
        # Checking quantity
        if self.product.available_quantity < self.quantity:
            raise ValidationError(dict(validation_error="No such quantity available"))
        elif self.quantity < 1:
            raise ValidationError(dict(validation_error="Min quantity is 1"))

    def validate_quantity_for_existing_product(self):
        # Checking quantity
        same_product = self.user.productorders.filter(is_active=True, product=self.product,
                                                 color=self.color)
        for param in self.product_params:
            same_product = same_product.filter(product_param=param)
        if same_product.exists():
            product_order = same_product.last()
            if product_order.quantity + self.quantity > self.product.available_quantity:
                raise ValidationError(dict(validation_error='Not available in such quantity'))