from django.contrib import admin
from core.models.order import *
from core.models.product import *
from django import forms


# - PRODUCT -

@admin.register(Catalog)
class CatalogModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent', 'is_active')


@admin.register(Brand)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'logo', 'is_active')


class ProductColorInline(admin.TabularInline):
    model = ProductColor
    extra = 0


class ProductImageInline(ProductColorInline):
    model = ProductImage
    extra = 0


class ProductGroupInline(admin.TabularInline):
    model = ProductGroup
    extra = 0


class ProductParamInline(ProductGroupInline):
    model = ProductParam
    extra = 0


@admin.register(ProductColor)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'color', 'title')


@admin.register(ProductImage)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image', 'is_active', 'is_slider')


# class ProductCreateForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    # add_form = ProductCreateForm

    fieldsets = (
        (None, {
            'fields': (
                'catalog',
                'brand',
                'title_uz',
                'title_en',
                'title_ru',
                'description_uz',
                'description_ru',
                'description_en',
                'price',
                'discount',
                'old_price',
                'is_active',
                'is_slider',
                'is_on_sale',
                'is_new',
                'is_stock',
                'status',
                'available_quantity'
            )
        }),
    )

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': (
    #             'catalog',
    #             'brand',
    #             'title_uz',
    #             'title_en',
    #             'title_ru',
    #             'description',
    #             'price',
    #             'discount',
    #             'old_price',
    #             'is_active',
    #             'is_slider',
    #             'is_on_sale',
    #             'is_new',
    #             'available_quantity'
    #         ),
    #     }),
    # )

    list_display = (
        'id',
        'title',
        'catalog',
        'brand',
        'price',
        'old_price',
        'discount',
        'rating',
        'is_active',
        'is_stock',
        'status',
    )

    list_filter = ('brand', 'catalog')
    save_on_top = True

    inlines = [ProductImageInline, ProductParamInline]

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return [inline(self.model, self.admin_site) for inline in self.inlines]


@admin.register(ProductGroup)
class ProductGroupModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(ProductParam)
class ProductParamModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'value', 'product', 'has_group')


@admin.register(ProductPrice)
class ProductPriceModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'param', 'price', 'available_count',)


@admin.register(PromoCode)
class PromoCodeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'is_active')


@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'id')


@admin.register(ReviewImage)
class ReviewImageModelAdmin(admin.ModelAdmin):
    list_display = ('review', 'photo')


@admin.register(Rating)
class ProductRatingModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'rate', 'product', 'review')


@admin.register(Delivery)
class DeliveryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'region', 'delivery_price')


@admin.register(Region)
class RegionModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uz', 'name_en', 'name_ru')

    # def has_add_permission(self, request):
    #     return False


# - ORDER -

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


@admin.register(Comment)
class CommentClassModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'user', 'text', 'is_active')
