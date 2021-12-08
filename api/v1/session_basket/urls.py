from django.urls import path
from . import views

urlpatterns = [
    # ----------------------Session Basket ----------------------
    path('basket/create/', views.TemporaryBasketCreateApi.as_view()),
]