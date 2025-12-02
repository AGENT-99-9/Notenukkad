from django.urls import path
from .views import SignupView, ProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import SignupView, ProfileView, FavoriteListView, ToggleFavoriteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('favorites/', FavoriteListView.as_view(), name='favorite-list'),
    path('favorites/<int:pk>/', ToggleFavoriteView.as_view(), name='toggle-favorite'),
]
