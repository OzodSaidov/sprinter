from django.urls import path
from . import views


urlpatterns = [
    path('me/create/', views.UserMeCreateView.as_view()),
    # path('me/', ),
    # path('me/update/', ),
]
