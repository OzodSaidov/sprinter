from modeltranslation.translator import translator, TranslationOptions
from core.models.product import Catalog, ProductColor, Product, Comment


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


translator.register(Catalog, CatalogTranslationOptions)
translator.register(ProductColor, ColorTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(Comment, CommentTranslationOptions)
