from django.db import transaction
from django.db.models import Avg
from rest_framework import serializers

from api.v1.product.services.round_avg import Round
from api.v1.product.validators import ReviewCreateValidator
from core.models import Catalog, Brand, Product, ProductImage, Rating, ProductColor, ProductParam, ProductPrice, Review, \
    ReviewImage, Comment
from sprinter_settings import settings


class CatalogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = [
            'id',
            'title',
            'parent',
            'is_active',
            'image',
            'sub_catalogs',
        ]
        extra_kwargs = {
            'sub_catalogs': {'read_only': True},
        }

    def to_representation(self, instance: Catalog):
        response = super().to_representation(instance)
        response['sub_catalogs'] = CatalogListSerializer(instance.sub_catalogs.all(), many=True).data
        return response


class CatalogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = (
            'id',
            'title_ru',
            'title_uz',
            'title_en',
            'image',
            'parent',
            'is_active',
        )


class CatalogRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = (
            'id',
            'title_ru',
            'title_uz',
            'title_en',
            'image',
            'parent',
            'is_active',
        )

    def to_representation(self, instance: Catalog):
        response = super().to_representation(instance)
        response['sub_catalogs'] = CatalogListSerializer(instance.sub_catalogs.all(), many=True).data
        return response


class CatalogRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = (
            'id',
            'title',
            'image',
            'parent',
            'is_active',
        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['sub_catalogs'] = CatalogListSerializer(instance.sub_catalogs.all(), many=True).data
        return response


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'title',
            'logo'
        )


class BrandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'title',
            'logo',
            'is_active'
        )


class BrandRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'title',
            'logo',
            'is_active'
        )


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            'id',
            'product',
            'image',
            'is_active'
        )


class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = (
            'id',
            'user',
            'product',
            'rate'
        )


class ProductListSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True)
    rating = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = (
            'id',
            'brand',
            'title',
            'description',
            'price',
            'old_price',
            'discount',
            'image',
            'rating',
            'is_new',
        )

    def to_representation(self, instance):
        data = super(ProductListSerializer, self).to_representation(instance)
        data['image'] = ProductImageSerializer(instance.images.filter(is_active=True).first(),
                                               context=self.context).data
        return data


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = (
            'id',
            'color',
            # 'title',
        )


class ProductParamPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = (
            'price',
        )


class ProductParamSerializer(serializers.ModelSerializer):
    price = serializers.PrimaryKeyRelatedField(source='prices', queryset=ProductPrice.objects.all())

    class Meta:
        model = ProductParam
        fields = (
            'id',
            # 'product',
            # 'group',
            'key',
            'value',
            'price',
            # 'is_important',
        )

    def to_representation(self, instance: ProductParam):
        data = super(ProductParamSerializer, self).to_representation(instance)
        if hasattr(instance, 'prices'):
            data['price'] = instance.prices.price
        return data


class ProductCreateSerializer(serializers.ModelSerializer):
    image = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False),
        required=True,
        write_only=True,
        allow_empty=True
    )

    class Meta:
        model = Product
        fields = (
            'id',
            'brand',
            'title_uz',
            'title_ru',
            'title_en',
            'description_uz',
            'description_ru',
            'description_en',
            'price',
            'old_price',
            'image',
            'is_active',
            'available_quantity',
            'is_slider',
            'is_on_sale',
            'is_new',

        )

    def create(self, validated_data):
        images = validated_data.pop('image', [])
        with transaction.atomic():
            product = super(ProductCreateSerializer, self).create(validated_data)
            for image in images:
                ProductImage.objects.create(product=product, image=image)
        return product


class ProductRetrieveUpdateSerializer(serializers.ModelSerializer):
    image = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False),
        required=True,
        write_only=True,
        allow_empty=True
    )
    rating = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = (
            'id',
            'brand',
            'title_uz',
            'title_ru',
            'title_en',
            'description_uz',
            'description_ru',
            'description_en',
            'price',
            'old_price',
            'rating',
            'image',
            'available_quantity',
            'is_new'
        )

    def update(self, instance, validated_data):
        images = validated_data.pop('image', [])
        with transaction.atomic():
            for image in images:
                ProductImage.objects.create(product=instance, image=image)
        return super(ProductRetrieveUpdateSerializer, self).update(instance, validated_data)


class ProductRetrieveSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(read_only=True)
    colors = serializers.PrimaryKeyRelatedField(queryset=ProductColor.objects.all(), many=True)
    params = serializers.SerializerMethodField(read_only=True)
    important_params = serializers.SerializerMethodField(read_only=True)
    rating = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = (
            'id',
            'brand',
            'title',
            'description',
            'price',
            'old_price',
            'rating',
            'images',
            'colors',
            'is_new',
            'available_quantity',
            'params',
            'important_params',
        )

    def get_images(self, obj):
        request = self.context['request']
        url_scheme = '{}://{}{}'.format(request.scheme, request.get_host(), settings.MEDIA_URL)
        return list(map(
            lambda item: {
                "IMAGE_URL": ''.join([url_scheme, item[0]]),
                "COLOR": item[1]
            }, obj.images.all().values_list('image', 'color')
        ))

    def get_params(self, obj):
        params = obj.params.filter(group__isnull=True).values_list('key', 'value')
        result = {}
        if params:
            result = {item[0]: item[1] for item in params}
        return result

    def get_important_params(self, obj):
        groups = set(
            obj.params.filter(group__isnull=False).values_list('group__title', flat=True)
        )
        result = [
            {
                "group": group,
                "params": [
                    dict(id=item[0], param=item[1], price=item[2])
                    for item in obj.params.filter(group__title=group).values_list('id', 'value', 'prices__price')
                ]
            }
            for group in groups
        ]
        return result

    def to_representation(self, instance: Product):
        data = super(ProductRetrieveSerializer, self).to_representation(instance)
        if instance.colors:
            data['colors'] = instance.colors.all().values('id', 'color')
        return data


class ReviewImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = (
            'id',
            'review',
            'photo',
        )


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = (
            'id',
            'rate'
        )


class ReviewListSerializer(serializers.ModelSerializer):
    rate = serializers.PrimaryKeyRelatedField(read_only=True)
    images = ReviewImagesSerializer(source='reviewimage_set', many=True)

    class Meta:
        model = Review
        fields = (
            'id',
            'user',
            'rate',
            'comment',
            'images',
            'created_at',
        )

    def to_representation(self, instance: Review):
        data = super(ReviewListSerializer, self).to_representation(instance)
        data['rate'] = instance.product_rating.rate
        data['created_at'] = instance.created_at.strftime('%d.%m.%Y')
        data['user'] = instance.user.full_name
        return data


class ReviewCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False),
        required=False,
        write_only=True,
        allow_empty=True
    )
    rating = serializers.FloatField(required=False)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = (
            'id',
            'user',
            'product',
            'comment',
            'like',
            'rating',
            'images',
        )
        validators = [ReviewCreateValidator()]

    def create(self, validated_data):
        rate = validated_data.pop('rating', 0)
        images = validated_data.pop('images', [])
        user = validated_data.get('user')
        product = validated_data.get('product')

        with transaction.atomic():
            review = super(ReviewCreateSerializer, self).create(validated_data)
            for image in images:
                ReviewImage.objects.create(review=review, photo=image)

            Rating.objects.create(user=user, product=product, rate=rate, review=review)

        return review

    def to_representation(self, instance: Review):
        data = super(ReviewCreateSerializer, self).to_representation(instance)
        data['rating'] = instance.product_rating.rate
        return data


class RatingCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Rating
        fields = (
            'id',
            'user',
            'product',
            'rate',
        )


class RatingUpdateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Rating
        fields = (
            'id',
            'rate',
            'user',
            'product',
        )


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'parent',
            'text',
            'user',
            'is_active',
            'created_at',
            'sub_comments',
        ]
        extra_kwargs = {
            'sub_comments': {'read_only': True},
        }

    def to_representation(self, instance: Comment):
        data = super().to_representation(instance)
        data['sub_comments'] = CommentListSerializer(instance.sub_comments.all(), many=True).data
        if instance.user:
            data['user'] = instance.user.full_name
        data['created_at'] = instance.created_at.strftime('%d %b, %Y - %H:%M')
        return data


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = (
            'id',
            'parent',
            'text',
            'user',
            'sub_comments',
        )
