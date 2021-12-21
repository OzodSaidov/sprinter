from django.urls import path
from . import views

urlpatterns = [
    # ----------------------CATALOG----------------------
    path('catalog/list/', views.CatalogListView.as_view()),
    path('catalog/<int:id>/sub_catalogs/', views.SubCatalogListView.as_view()),
    # path('catalog/create/', views.CatalogCreateView.as_view()),
    # path('catalog/edit/<int:pk>/', views.CatalogEditView.as_view()),
    # path('catalog/detail/<int:pk>/', views.CatalogRetrieveView.as_view()),
    # path('catalog/delete/<int:pk>/', views.CatalogDeleteView.as_view()),

    # ----------------------BRAND----------------------
    path('brand/list/', views.BrandListView.as_view()),
    # path('brand/create/', views.BrandCreateView.as_view()),
    # path('brand/<int:pk>/', views.BrandRetrieveUpdateDestroyView.as_view()),

    # ----------------------PRODUCT----------------------
    path('list/', views.ProductListView.as_view()),
    path('list/new/', views.ProductNewListView.as_view()),
    path('<int:id>/similars/', views.SimilarProductListView.as_view()),
    # path('create/', views.ProductCreateView.as_view()),
    # path('edit/<int:pk>/', views.ProductEditView.as_view()),
    path('detail/<int:pk>/', views.ProductRetrieveView.as_view()),
    # path('delete/<int:pk>/', views.ProductDeleteView.as_view()),

    # ----------------------PRODUCT COLOR----------------------
    # path('color/list/', views.ProductColorListView.as_view()),
    # path('color/create/', views.ProductColorCreateView.as_view()),
    # path('color/edit/<int:pk>/', views.ProductColorEditView.as_view()),
    # path('color/detail/<int:pk>/', views.ProductColorRetrieveView.as_view()),
    # path('color/delete/<int:pk>/', views.ProductColorDeleteView.as_view()),

    # ----------------------PRODUCT IMAGE----------------------
    # path('image/list/', views.ProductImageListView.as_view()),
    # path('image/upload/', views.ProductImageUploadView.as_view()),
    # path('image/detail/<int:pk>/', views.ProductImageRetrieveView.as_view()),
    # path('image/delete/<int:pk>/', views.ProductImageDeleteView.as_view()),

    # ----------------------PRODUCT GROUP----------------------
    # path('group/list/', views.ProductGroupListView.as_view()),
    # path('group/create/', views.ProductGroupCreateView.as_view()),
    # path('group/edit/<int:pk>/', views.ProductGroupEditView.as_view()),
    # path('group/detail/<int:pk>/', views.ProductGroupRetrieveView.as_view()),
    # path('group/delete/<int:pk>/', views.ProductGroupDeleteView.as_view()),

    # ----------------------PRODUCT PARAMS----------------------
    # path('param/list/', views.ProductParamListView.as_view()),
    # path('param/create/', views.ProductParamCreateView.as_view()),
    # path('param/edit/<int:pk>/', views.ProductParamEditView.as_view()),
    # path('param/detail/<int:pk>/', views.ProductParamRetrieveView.as_view()),
    # path('param/delete/<int:pk>/', views.ProductParamDeleteView.as_view()),

    # ----------------------PRODUCT PRICE----------------------
    # path('price/list/', views.ProductPriceListView.as_view()),
    # path('price/create/', views.ProductPriceCreateView.as_view()),
    # path('price/edit/<int:pk>/', views.ProductPriceEditView.as_view()),
    # path('price/delete/<int:pk>/', views.ProductPriceDeleteView.as_view()),

    # ----------------------PROMO CODE----------------------
    # path('promocode/list/', views.PromoCodeListView.as_view()),
    # path('promocode/create/', views.PromoCodeCreateView.as_view()),
    # path('promocode/edit/<int:pk>/', views.PromoCodeEditView.as_view()),
    # path('promocode/delete/<int:pk>/', views.PromoCodeDeleteView.as_view()),

    # ----------------------COMMENT----------------------
    path('comment/list/', views.CommentListView.as_view()),
    path('comment/create/', views.CommentCreateView.as_view()),
    # path('comment/edit/<int:pk>/', views.CommentEditView.as_view()),
    # path('comment/detail/<int:pk>/', views.CommentRetrieveView.as_view()),
    # path('comment/delete/<int:pk>/', views.CommentDeleteView.as_view()),

    # ----------------------RATING----------------------
    # path('rating/list/', views.RatingListView.as_view()),
    path('rating/create/', views.RatingCreateView.as_view()),
    path('rating/update/<int:pk>/', views.RatingUpdateView.as_view()),
    # path('rating/delete/<int:pk>/', views.RatingDeleteView.as_view()),

    # ----------------------REVIEW----------------------
    path('review/list/', views.ReviewListView.as_view()),
    path('review/create/', views.ReviewCreateView.as_view()),
    # path('review/edit/<int:pk>/', views.ReviewEditView.as_view()),
    # path('review/delete/<int:pk>/', views.ReviewDeleteView.as_view()),

    # ----------------------REVIEW IMAGE----------------------
    # path('review/image/list/', views.ReviewImageListView.as_view()),
    # path('review/image/upload/', views.ReviewImageUploadView.as_view()),
    # path('review/image/detail/<int:pk>/', views.ReviewImageRetrieveView.as_view()),
    # path('review/image/delete/<int:pk>/', views.ReviewImageDeleteView.as_view()),

    path('slider/', views.ProductSliderView.as_view()),
]
