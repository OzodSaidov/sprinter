from django.db import transaction
from django.db.models import Avg
from rest_framework import serializers

from core.models import Catalog, Brand, Product, ProductImage, Rating, ProductColor


class CatalogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = [
            'id',
            'title',
            'parent',
            'is_active',
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
            'image',
            'rating',
        )

    def to_representation(self, instance):
        data = super(ProductListSerializer, self).to_representation(instance)
        data['image'] = ProductImageSerializer(instance.images.filter(is_active=True).first(),
                                               context=self.context).data
        return data

    def get_rating(self, instance):
        return instance.rating_set.all().aggregate(rating=Avg('rate'))


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
            'image',
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
            'image',
        )

    def update(self, instance, validated_data):
        images = validated_data.pop('image', [])
        with transaction.atomic():
            for image in images:
                ProductImage.objects.create(product=instance, image=image)
        return super(ProductRetrieveUpdateSerializer, self).update(instance, validated_data)


class ProductRetrieveSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'brand',
            'title',
            'description',
            'price',
            'image',
        )

    def to_representation(self, instance: Product):
        data = super(ProductRetrieveSerializer, self).to_representation(instance)
        data['image'] = ProductImageSerializer(instance.images.all(), many=True,
                                               context=self.context).data
        return data


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = (
            'id',
            'color',
            'title',
        )