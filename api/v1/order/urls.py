import http

from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # Order
    path('list/', OrderListApiView.as_view()),
    path('create/', OrderCreateApiView.as_view()),
    path('update/<int:pk>/', OrderUpdateApiView.as_view()),
    path('detail/<int:pk>/', OrderDetailApiView.as_view()),
    path('delete/<int:pk>/', OrderDestroyApiView.as_view()),

    # Product Order - Exact order of some product, which is added to basket
    path('product-order/list/', ProductOrderListApiView.as_view()),
    path('product-order/create/', ProductOrderCreateApiView.as_view()),
    path('product-order/update/<int:pk>/', ProductOrderUpdateApiView.as_view()),
    path('product-order/detail/<int:pk>/', ProductOrderDetailApiView.as_view()),
    path('product-order/delete/<int:pk>/', ProductOrderDestroyApiView.as_view()),

    # Basket - collection of product orders
    path('basket/list/', BasketListApiView.as_view()),
    # path('basket/create/', BasketCreateApiView.as_view()),
    # path('basket/update/<int:pk>/', BasketUpdateApiView.as_view()),
    # path('basket/detail/<int:pk>/', BasketDetailApiView.as_view()),
    # path('basket/delete/<int:pk>/', BasketDestroyApiView.as_view()),
    path('basket/current/', CurrentBasketApiView.as_view()),
    path('basket/current/products/', CurrentBasketProductsListApiView.as_view()),
    path('basket/products/count/', CurrentBasketProductNumberApiView.as_view()),
]