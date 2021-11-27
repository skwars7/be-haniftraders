from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('token/', views.MyObtainTokenPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
