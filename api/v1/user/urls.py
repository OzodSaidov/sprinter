from django.urls import path
from . import views

urlpatterns = [
    path('me/create/', views.UserMeCreateView.as_view()),
    path('me/', views.UserMeView.as_view()),
    path('verification/', views.VerifyAPIView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('password-reset/', views.UserResetPasswordView.as_view()),
    path('address/', views.AddressListCreateView.as_view()),
    # path('address/list/', views.AddressListView.as_view()),
    # path('me/update/', ),
]
