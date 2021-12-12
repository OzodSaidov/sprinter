from django.urls import path
from . import views

urlpatterns = [
    # ----------------------Session Basket ----------------------
    path('basket/create/', views.TemporaryBasketCreateApi.as_view()),
    path('basket/update/', views.TemporaryBasketUpdateApi.as_view()),
    path('basket/list/', views.TemporaryBasketListApi.as_view()),
    path('basket/remove/', views.TemporaryBasketDeleteApi.as_view()),
]

