from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.user.urls')),
    path('order/', include('api.v1.order.urls')),
]
