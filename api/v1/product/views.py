from rest_framework import generics
from rest_framework.permissions import AllowAny

from core.models import *
from .filters import ProductFilter, ReviewFilter
from .serializers import *


class CatalogListView(generics.ListAPIView):
    serializer_class = CatalogListSerializer
    queryset = Catalog.objects.filter(parent=None)
    permission_classes = [AllowAny]


class CatalogCreateView(generics.CreateAPIView):
    serializer_class = CatalogCreateSerializer


class CatalogEditView(generics.RetrieveUpdateAPIView):
    """For CMS"""
    serializer_class = CatalogRetrieveUpdateSerializer
    queryset = Catalog.objects.all()


class CatalogRetrieveView(generics.RetrieveAPIView):
    """For site"""
    serializer_class = CatalogRetrieveSerializer
    queryset = Catalog.objects.all()


class CatalogDeleteView(generics.DestroyAPIView):
    queryset = Catalog.objects.all()


class BrandListView(generics.ListAPIView):
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()


class BrandCreateView(generics.CreateAPIView):
    serializer_class = BrandCreateSerializer


class BrandRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrandRetrieveUpdateSerializer
    queryset = Brand.objects.all()


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    permission_classes = [AllowAny]
    filterset_class = ProductFilter


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer


class ProductEditView(generics.RetrieveUpdateAPIView):
    """For CMS"""
    serializer_class = ProductRetrieveUpdateSerializer
    queryset = Product.objects.all()


class ProductRetrieveView(generics.RetrieveAPIView):
    """For site"""
    serializer_class = ProductRetrieveSerializer
    permission_classes = [AllowAny]
    queryset = Product.objects.all()


# class ProductDeleteView(generics.DestroyAPIView):
#     queryset = Product.objects.all()


# class ProductColorListView(generics.ListAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = ProductColor.objects.all()


# class ProductColorCreateView(generics.CreateAPIView):
#     serializer_class = None
#     # permission_classes = None


# class ProductColorEditView(generics.RetrieveUpdateAPIView):
#     """For CMS"""
#     serializer_class = None
#     # permission_classes = None
#     queryset = ProductColor.objects.all()


# class ProductColorRetrieveView(generics.RetrieveAPIView):
#     """For site"""
#     serializer_class = None
#     # permission_classes = None
#     queryset = ProductColor.objects.all()


# class ProductColorDeleteView(generics.DestroyAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = ProductColor.objects.all()


# class ProductImageListView(generics.ListAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = ProductImage.objects.all()


# class ProductImageUploadView(generics.CreateAPIView):
#     serializer_class = None
#     # permission_classes = None


# class ProductImageRetrieveView(generics.RetrieveAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = ProductImage.objects.all()


# class ProductImageDeleteView(generics.DestroyAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = ProductImage.objects.all()


# class ProductGroupListView(generics.ListAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = ProductGroup.objects.all()


# class ProductGroupCreateView(generics.CreateAPIView):
#     serializer_class = None
#     # permission_classes = None


# class ProductGroupEditView(generics.RetrieveUpdateAPIView):
#     """For CMS"""
#     serializer_class = None
#     # permission_classes = None
#     queryset = ProductGroup.objects.all()


# class ProductGroupRetrieveView(generics.RetrieveAPIView):
#     """For site"""
#     serializer_class = None
#     # permission_classes = None
#     queryset = ProductGroup.objects.all()


# class ProductGroupDeleteView(generics.DestroyAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = ProductGroup.objects.all()


class ProductParamListView(generics.ListAPIView):
    serializer_class = ProductParamSerializer
    # permission_classes = None
    queryset = ProductParam.objects.all()


# class ProductParamCreateView(generics.CreateAPIView):
#     serializer_class = None
#     # permission_classes = None


# class ProductParamEditView(generics.RetrieveUpdateAPIView):
#     """For CMS"""
#     serializer_class = None
#     # permission_classes = None
#     queryset = ProductParam.objects.all()


class ProductParamRetrieveView(generics.RetrieveAPIView):
    """For site"""
    serializer_class = ProductParamSerializer
    # permission_classes = None
    queryset = ProductParam.objects.all()


# class ProductParamDeleteView(generics.DestroyAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = ProductParam.objects.all()


# class ProductPriceListView(generics.ListAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = ProductPrice.objects.all()


# class ProductPriceCreateView(generics.CreateAPIView):
#     serializer_class = None
#     # permission_classes = None


# class ProductPriceEditView(generics.RetrieveUpdateAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = ProductPrice.objects.all()


# class ProductPriceDeleteView(generics.DestroyAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = ProductPrice.objects.all()


# class PromoCodeListView(generics.ListAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = PromoCode.objects.all()


# class PromoCodeCreateView(generics.CreateAPIView):
#     serializer_class = None
#     # permission_classes = None


# class PromoCodeEditView(generics.RetrieveUpdateAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = PromoCode.objects.all()


# class PromoCodeDeleteView(generics.DestroyAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = PromoCode.objects.all()


# class CommentListView(generics.ListAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = Comment.objects.all()


# class CommentCreateView(generics.CreateAPIView):
#     serializer_class = None
#     # permission_classes = None


# class CommentEditView(generics.RetrieveUpdateAPIView):
#     """For CMS"""
#     serializer_class = None
#     # permission_classes = None
#     queryset = Comment.objects.all()


# class CommentRetrieveView(generics.RetrieveAPIView):
#     """For site"""
#     serializer_class = None
#     # permission_classes = None
#     queryset = Comment.objects.all()


# class CommentDeleteView(generics.DestroyAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = Comment.objects.all()

#
# class RatingListView(generics.ListAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = Rating.objects.all()


class RatingCreateView(generics.CreateAPIView):
    serializer_class = RatingCreateSerializer
    # permission_classes = None


class RatingUpdateView(generics.UpdateAPIView):
    serializer_class = RatingUpdateSerializer
    # permission_classes = None
    queryset = Rating.objects.all()


# class RatingDeleteView(generics.DestroyAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = Rating.objects.all()


class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewListSerializer
    permission_classes = [AllowAny]
    queryset = Review.objects.all()
    filterset_class = ReviewFilter


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewCreateSerializer
    # permission_classes = None


# class ReviewEditView(generics.RetrieveUpdateAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = Review.objects.all()


# class ReviewDeleteView(generics.DestroyAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = Review.objects.all()


# class ReviewImageListView(generics.ListAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = ReviewImage.objects.all()


# class ReviewImageUploadView(generics.CreateAPIView):
#     serializer_class = None
#     # permission_classes = None


# class ReviewImageRetrieveView(generics.RetrieveAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = ReviewImage.objects.all()


# class ReviewImageDeleteView(generics.DestroyAPIView):
#     serializer_class = None
#     # permission_classes = None
#     queryset = ReviewImage.objects.all()
