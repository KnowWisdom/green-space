from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    UserListView,
    CustomUserView,
    SignInUserView,
    SignOutUserView,
    DeleteUserView,
    ProfileView
)

app_name = 'users'

urlpatterns = [
    path('', UserListView.as_view(), name="user-list"),
    path('profile/', ProfileView.as_view()),
    path('signup/', CustomUserView.as_view(), name="user-create"),
    path('signin/', SignInUserView.as_view(), name="user-detail"),
    path('signin/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('signout/', SignOutUserView.as_view(), name="logout"),
    path("delete/", DeleteUserView.as_view(), name="delete"),
]
