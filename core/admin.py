from django.contrib import admin

# Register your models here.

from core.models.order import *
from core.models.product import *


####################### - PRODUCT - #######################

class CatalogModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent', 'is_active')


class ColorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'icon', 'is_active')


class BrandModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'logo', 'is_active')


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'catalog', 'brand', 'is_active')


class ProductParamModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'value', 'product', 'has_group')


class ProductPriceModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'param', 'price', 'available_count',)


class PromoCodeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'is_active')


class BrandCodeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active')


admin.site.register(Catalog, CatalogModelAdmin)
admin.site.register(Color, ColorModelAdmin)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(ProductParam, ProductParamModelAdmin)
admin.site.register(ProductPrice, ProductPriceModelAdmin)
admin.site.register(PromoCode, PromoCodeModelAdmin)
admin.site.register(Brand, BrandModelAdmin)

####################### - PRODUCT - #######################

####################### - ORDER - #######################


class ProductOrderClassModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity')


class BasketClassModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active')


class OrderClassModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'basket', 'payment_type',
                    'order_status', 'payment_status',
                    'promocode', 'is_active')


admin.site.register(ProductOrder, ProductOrderClassModelAdmin)
admin.site.register(Basket, BasketClassModelAdmin)
admin.site.register(Order, OrderClassModelAdmin)


####################### - ORDER - #######################


####################### - Comment, Rating - #######################


class CommentClassModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'user', 'title', 'is_active')


admin.site.register(Comment, CommentClassModelAdmin)