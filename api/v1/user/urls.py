from django.urls import path

from user.token import MyTokenObtainPairView
from . import views


urlpatterns = [
    path('me/create/', views.UserMeCreateView.as_view()),
    path('phone-verification/', views.PhoneVerifyAPIView.as_view()),
    path('login/', views.LoginView.as_view())
    # path('me/', ),
    # path('me/update/', ),
]
