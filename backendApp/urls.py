from django.urls import path,include
from django.contrib import admin

from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RegisterUserView

urlpatterns = [
    path('signup/', RegisterUserView.as_view(), name='signup'),
    path('', TokenObtainPairView.as_view(), name='login'),  # JWT login
]
