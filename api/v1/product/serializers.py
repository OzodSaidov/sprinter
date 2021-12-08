from django.db import transaction
from django.db.models import Avg
from rest_framework import serializers
from core.models import Catalog, Brand, Product, ProductImage, Rating, ProductColor, ProductParam, ProductPrice, Review, \
    ReviewImage


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
    rating = serializers.SerializerMethodField(read_only=True)

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
            'status',
        )

    def to_representation(self, instance):
        data = super(ProductListSerializer, self).to_representation(instance)
        data['image'] = ProductImageSerializer(instance.images.filter(is_active=True).first(),
                                               context=self.context).data
        return data

    def get_rating(self, instance):
        return instance.rating_set.all().aggregate(rating=Avg('rate'))


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = (
            'id',
            'color',
            'title',
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
            'status',

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
            'available_quantity',
        )

    def update(self, instance, validated_data):
        images = validated_data.pop('image', [])
        with transaction.atomic():
            for image in images:
                ProductImage.objects.create(product=instance, image=image)
        return super(ProductRetrieveUpdateSerializer, self).update(instance, validated_data)


class ProductRetrieveSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True)
    colors = serializers.PrimaryKeyRelatedField(queryset=ProductColor.objects.all(), many=True)
    params = serializers.SerializerMethodField(read_only=True)
    important_params = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'brand',
            'title',
            'description',
            'price',
            'old_price',
            'image',
            'colors',
            'status',
            'available_quantity',
            'params',
            'important_params',
        )

    def get_params(self, obj):
        params = obj.params.filter(group__isnull=True).values_list('key', 'value')
        result = {}
        if params:
            result = {_[0]: _[1] for _ in params}
        return result

    def get_important_params(self, obj):
        groups = set(
            obj.params.filter(group__isnull=False).values_list('group__title', flat=True)
        )
        result = {
            group: {_[0]: _[1] for _ in obj.params.filter(group__title=group).values_list('value', 'prices__price')}
            for group in groups
        }
        return result

    def to_representation(self, instance: Product):
        data = super(ProductRetrieveSerializer, self).to_representation(instance)
        data['image'] = ProductImageSerializer(instance.images.all(), many=True,
                                               context=self.context).data
        if instance.colors:
            data['colors'] = instance.colors.all().values_list('color', flat=True)
        return data


class ReviewImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = (
            'id',
            'review',
            'photo',
        )


class ReviewListSerializer(serializers.ModelSerializer):
    rating = serializers.PrimaryKeyRelatedField(source='product_rating', read_only=True)
    images = ReviewImagesSerializer(many=True)

    class Meta:
        model = Review
        fields = (
            'id',
            'user',
            'rating',
            'comment',
            'images',
        )

    def to_representation(self, instance: Review):
        data = super(ReviewListSerializer, self).to_representation(instance)
        if instance.product_rating:
            data['rating'] = instance.product_rating.rate
        return data


class ReviewCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False),
        required=True,
        write_only=True,
        allow_empty=True
    )
    rating = serializers.FloatField()
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
