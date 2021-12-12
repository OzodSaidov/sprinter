from django.contrib import admin
from core.models.order import *
from core.models.product import *


# - PRODUCT -

class CatalogModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent', 'is_active')


class ColorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'color', 'product')


class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image', 'is_active')


class BrandModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'logo', 'is_active')


class ProductColorInline(admin.StackedInline):
    model = ProductColor
    extra = 1


class ProductImageInline(ProductColorInline):
    model = ProductImage
    extra = 1


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'catalog', 'brand', 'price', 'old_price', 'discount', 'rating', 'is_active')
    list_filter = ('brand', 'catalog')

    inlines = (
        ProductImageInline,
        # ProductColorInline,
    )


class ProductGroupModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class ProductParamModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'value', 'product', 'has_group')


class ProductPriceModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'param', 'price', 'available_count',)


class PromoCodeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'is_active')


class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'id')


class ReviewImageModelAdmin(admin.ModelAdmin):
    list_display = ('review', 'photo')


class ProductRatingModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'rate', 'product', 'review')


admin.site.register(Catalog, CatalogModelAdmin)
admin.site.register(ProductColor, ColorModelAdmin)
admin.site.register(ProductImage, ImageModelAdmin)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(ProductParam, ProductParamModelAdmin)
admin.site.register(ProductPrice, ProductPriceModelAdmin)
admin.site.register(PromoCode, PromoCodeModelAdmin)
admin.site.register(Brand, BrandModelAdmin)
admin.site.register(Review, ReviewModelAdmin)
admin.site.register(ReviewImage, ReviewImageModelAdmin)
admin.site.register(ProductGroup, ProductGroupModelAdmin)
admin.site.register(Rating, ProductRatingModelAdmin)


####################### - PRODUCT - #######################

####################### - ORDER - #######################


class ProductOrderClassModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity')

    # def save_related(self, request, form, formsets, change):
    #     super(ProductOrderClassModelAdmin, self).save_related(request, form, formsets, change)
    #     print(form.instance.product_param.values_list('group', flat=True))
    #     # raise ValidationError('Not possible')


class BasketClassModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active')


class OrderClassModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payment_type',
                    'order_status', 'payment_status',
                    'promocode', 'is_active')
    list_filter = (
        'order_status',
    )

    def get_items(self, obj):
        text = ''
        for index, product_order in enumerate(obj.basket.products.all()):
            params = '\n'.join([f"{param.key} : {param.value}" for param in product_order.product_param.all()])
            text += '{}. {}, {} шт\nЦвет: {}\n{}\nЦена: {}\n\n'.format(index + 1,
                                                                       product_order.product.title,
                                                                       product_order.quantity,
                                                                       product_order.color.title,
                                                                       params,
                                                                       product_order.price)
        return text

    get_items.short_description = 'Товары'
    exclude = ('basket', 'is_active')
    readonly_fields = ('promocode', 'price', 'get_items')


admin.site.register(ProductOrder, ProductOrderClassModelAdmin)
admin.site.register(Basket, BasketClassModelAdmin)
admin.site.register(Order, OrderClassModelAdmin)


####################### - ORDER - #######################


####################### - Comment, Rating - #######################


class CommentClassModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'user', 'text', 'is_active')


admin.site.register(Comment, CommentClassModelAdmin)
