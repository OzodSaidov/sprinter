from django.urls import path, include

urlpatterns = [
    path('payme/', include('api.v1.payment.payme.urls')),
    path('click/', include('api.v1.payment.click.urls')),
]
