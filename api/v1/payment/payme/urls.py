from django.urls import path, include
from .views import PayOrderWithPaymeApi

urlpatterns = [
    path('pay-order/', PayOrderWithPaymeApi.as_view() ),
]
