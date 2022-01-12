from django.urls import path
from . import views


urlpatterns = [
    # ----------------------Back Call----------------------
    path('create/', views.BackCallCreateView.as_view()),
]
