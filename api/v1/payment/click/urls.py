from django.urls import path, include

urlpatterns = [
    path('payme/', include('api.v1.user.urls')),
    path('click/', include('api.v1.order.urls')),
]
