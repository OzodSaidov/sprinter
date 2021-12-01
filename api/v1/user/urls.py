from django.urls import path

from user.token import MyTokenObtainPairView
from . import views


urlpatterns = [
    path('me/create/', views.UserMeCreateView.as_view()),
    path('verification/', views.VerifyAPIView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('password-reset/', views.UserResetPasswordView.as_view()),
    # path('me/', ),
    # path('me/update/', ),
]
