from django.urls import path, include

from api.v1.product.views import RegionListView

urlpatterns = [
    path('user/', include('api.v1.user.urls')),
    path('order/', include('api.v1.order.urls')),
    path('product/', include('api.v1.product.urls')),
    path('session/', include('api.v1.session_basket.urls')),
    path('payment/', include('api.v1.payment.urls')),
    path('search/', include('api.v1.search.urls')),
    path('regions/', RegionListView.as_view()),
]
