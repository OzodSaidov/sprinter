from modeltranslation.translator import translator, TranslationOptions
from core.models.product import Catalog, ProductColor, Product, Comment, ProductParam, ProductGroup


class CatalogTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )


class ColorTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )


class ProductTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )


class CommentTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )


class ProductParamTranslationOptions(TranslationOptions):
    fields = (
        'key',
        'value',
    )


class ProductGroupTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )


translator.register(Catalog, CatalogTranslationOptions)
translator.register(ProductColor, ColorTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(Comment, CommentTranslationOptions)
translator.register(ProductParam, ProductParamTranslationOptions)
translator.register(ProductGroup, ProductGroupTranslationOptions)