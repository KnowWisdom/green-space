from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *

app_name = 'users'

urlpatterns = [
    path('', UserListView.as_view(), name="user-list"),
    path('profile/', ProfileView.as_view()),
    path('signup/', CustomUserView.as_view(), name="user-create"),
    path('signin/', SignInUserView.as_view(), name="user-detail"),
    path('signin/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('signout/', SignOutUserView.as_view(), name="logout"),
    path("delete/", DeleteUserView.as_view(), name="delete"),
    path("following/", FollowingView.as_view(), name="user-follow"),
    path("followinglist/", FollowingListView.as_view(), name="user-following-list"),
    path("followedlist/", FollowedListView.as_view(), name="user-followed-list"),

]
