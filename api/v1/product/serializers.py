from rest_framework import serializers

from core.models import Catalog


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
        extra_kwargs = {
            'sub_catalogs': {'read_only': True},
            'title': {'read_only': True},
        }


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
