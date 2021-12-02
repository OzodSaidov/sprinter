from rest_framework import generics

from core.models import Catalog, Brand, Product, ProductColor, ProductImage, ProductGroup, ProductParam, ProductPrice, \
    PromoCode, Comment, Rating, Review, ReviewImage


class CatalogListView(generics.ListAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = Catalog.objects.all()


class CatalogCreateView(generics.CreateAPIView):
    serializer_class = None
    # permission_classes = None


class CatalogEditView(generics.RetrieveUpdateAPIView):
    """For CMS"""
    serializer_class = None
    # permission_classes = None
    queryset = Catalog.objects.all()


class CatalogRetrieveView(generics.RetrieveAPIView):
    """For site"""
    serializer_class = None
    # permission_classes = None
    queryset = Catalog.objects.all()


class CatalogDeleteView(generics.DestroyAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = Catalog.objects.all()


class BrandListView(generics.ListAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = Brand.objects.all()


class BrandCreateView(generics.CreateAPIView):
    serializer_class = None
    # permission_classes = None


class BrandEditView(generics.RetrieveUpdateAPIView):
    """For CMS"""
    serializer_class = None
    # permission_classes = None
    queryset = Brand.objects.all()


class BrandRetrieveView(generics.RetrieveAPIView):
    """For site"""
    serializer_class = None
    # permission_classes = None
    queryset = Brand.objects.all()


class BrandDeleteView(generics.DestroyAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = Brand.objects.all()


class ProductListView(generics.ListAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = Product.objects.all()


class ProductCreateView(generics.CreateAPIView):
    serializer_class = None
    # permission_classes = None


class ProductEditView(generics.RetrieveUpdateAPIView):
    """For CMS"""
    serializer_class = None
    # permission_classes = None
    queryset = Product.objects.all()


class ProductRetrieveView(generics.RetrieveAPIView):
    """For site"""
    serializer_class = None
    # permission_classes = None
    queryset = Product.objects.all()


class ProductDeleteView(generics.DestroyAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = Product.objects.all()


class ProductColorListView(generics.ListAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = ProductColor.objects.all()


class ProductColorCreateView(generics.CreateAPIView):
    serializer_class = None
    # permission_classes = None


class ProductColorEditView(generics.RetrieveUpdateAPIView):
    """For CMS"""
    serializer_class = None
    # permission_classes = None
    queryset = ProductColor.objects.all()


class ProductColorRetrieveView(generics.RetrieveAPIView):
    """For site"""
    serializer_class = None
    # permission_classes = None
    queryset = ProductColor.objects.all()


class ProductColorDeleteView(generics.DestroyAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = ProductColor.objects.all()


class ProductImageListView(generics.ListAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = ProductImage.objects.all()


class ProductImageUploadView(generics.CreateAPIView):
    serializer_class = None
    # permission_classes = None


class ProductImageRetrieveView(generics.RetrieveAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = ProductImage.objects.all()


class ProductImageDeleteView(generics.DestroyAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = ProductImage.objects.all()


class ProductGroupListView(generics.ListAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = ProductGroup.objects.all()


class ProductGroupCreateView(generics.CreateAPIView):
    serializer_class = None
    # permission_classes = None


class ProductGroupEditView(generics.RetrieveUpdateAPIView):
    """For CMS"""
    serializer_class = None
    # permission_classes = None
    queryset = ProductGroup.objects.all()


class ProductGroupRetrieveView(generics.RetrieveAPIView):
    """For site"""
    serializer_class = None
    # permission_classes = None
    queryset = ProductGroup.objects.all()


class ProductGroupDeleteView(generics.DestroyAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = ProductGroup.objects.all()


class ProductParamListView(generics.ListAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = ProductParam.objects.all()


class ProductParamCreateView(generics.CreateAPIView):
    serializer_class = None
    # permission_classes = None


class ProductParamEditView(generics.RetrieveUpdateAPIView):
    """For CMS"""
    serializer_class = None
    # permission_classes = None
    queryset = ProductParam.objects.all()


class ProductParamRetrieveView(generics.RetrieveAPIView):
    """For site"""
    serializer_class = None
    # permission_classes = None
    queryset = ProductParam.objects.all()


class ProductParamDeleteView(generics.DestroyAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = ProductParam.objects.all()


class ProductPriceListView(generics.ListAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = ProductPrice.objects.all()


class ProductPriceCreateView(generics.CreateAPIView):
    serializer_class = None
    # permission_classes = None


class ProductPriceEditView(generics.RetrieveUpdateAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = ProductPrice.objects.all()


class ProductPriceDeleteView(generics.DestroyAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = ProductPrice.objects.all()


class PromoCodeListView(generics.ListAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = PromoCode.objects.all()


class PromoCodeCreateView(generics.CreateAPIView):
    serializer_class = None
    # permission_classes = None


class PromoCodeEditView(generics.RetrieveUpdateAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = PromoCode.objects.all()


class PromoCodeDeleteView(generics.DestroyAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = PromoCode.objects.all()


class CommentListView(generics.ListAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = Comment.objects.all()


class CommentCreateView(generics.CreateAPIView):
    serializer_class = None
    # permission_classes = None


class CommentEditView(generics.RetrieveUpdateAPIView):
    """For CMS"""
    serializer_class = None
    # permission_classes = None
    queryset = Comment.objects.all()


class CommentRetrieveView(generics.RetrieveAPIView):
    """For site"""
    serializer_class = None
    # permission_classes = None
    queryset = Comment.objects.all()


class CommentDeleteView(generics.DestroyAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = Comment.objects.all()


class RatingListView(generics.ListAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = Rating.objects.all()


class RatingCreateView(generics.CreateAPIView):
    serializer_class = None
    # permission_classes = None


class RatingEditView(generics.RetrieveUpdateAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = Rating.objects.all()


class RatingDeleteView(generics.DestroyAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = Rating.objects.all()


class ReviewListView(generics.ListAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = Review.objects.all()


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = None
    # permission_classes = None


class ReviewEditView(generics.RetrieveUpdateAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = Review.objects.all()


class ReviewDeleteView(generics.DestroyAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = Review.objects.all()


class ReviewImageListView(generics.ListAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = ReviewImage.objects.all()


class ReviewImageUploadView(generics.CreateAPIView):
    serializer_class = None
    # permission_classes = None


class ReviewImageRetrieveView(generics.RetrieveAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = ReviewImage.objects.all()


class ReviewImageDeleteView(generics.DestroyAPIView):
    serializer_class = None
    # permission_classes = None
    queryset = ReviewImage.objects.all()