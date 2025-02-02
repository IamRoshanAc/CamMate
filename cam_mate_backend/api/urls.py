from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LoginAPIView, LogoutAPIView, UserProfileAPIView


urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('username/', UserProfileAPIView.as_view(), name='username'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]