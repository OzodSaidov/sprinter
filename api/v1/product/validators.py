from rest_framework.exceptions import ValidationError

from core.models import Review


class ReviewCreateValidator:

    def review_create(self, obj, *args, **kwargs):
        user = obj.get('user')
        product = obj.get('product')
        order = obj.get('order')
        if Review.objects.filter(user=user, product=product, order=order).exists():
            raise ValidationError({'error': 'You have already left a review for this product'})

    def __call__(self, *args, **kwargs):
        self.review_create(*args, **kwargs)
