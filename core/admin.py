from django.contrib import admin
from django import forms
# Register your models here.

from core.models.order import *
from core.models.product import *


####################### - PRODUCT - #######################

class CatalogModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent', 'is_active')


class ColorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'color', 'product')


class BrandModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'logo', 'is_active')


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'catalog', 'brand', 'price', 'is_active')


class ProductGroupModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class ProductParamModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'value', 'product', 'has_group')


class ProductPriceModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'param', 'price', 'available_count',)


class PromoCodeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'is_active')


class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'id')


class ReviewImageModelAdmin(admin.ModelAdmin):
    list_display = ('review', 'photo')


admin.site.register(Catalog, CatalogModelAdmin)
admin.site.register(ProductColor, ColorModelAdmin)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(ProductParam, ProductParamModelAdmin)
admin.site.register(ProductPrice, ProductPriceModelAdmin)
admin.site.register(PromoCode, PromoCodeModelAdmin)
admin.site.register(Brand, BrandModelAdmin)
admin.site.register(Review, ReviewModelAdmin)
admin.site.register(ReviewImage, ReviewImageModelAdmin)
admin.site.register(ProductGroup, ProductGroupModelAdmin)

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
    list_display = ('id', 'basket', 'payment_type',
                    'order_status', 'payment_status',
                    'promocode', 'is_active')
    list_filter = (
         'order_status',
    )

admin.site.register(ProductOrder, ProductOrderClassModelAdmin)
admin.site.register(Basket, BasketClassModelAdmin)
admin.site.register(Order, OrderClassModelAdmin)


####################### - ORDER - #######################


####################### - Comment, Rating - #######################


class CommentClassModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'user', 'title', 'is_active')


admin.site.register(Comment, CommentClassModelAdmin)
