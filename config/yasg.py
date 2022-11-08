from django.conf.urls import url
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from drf_yasg import openapi

schema_url_patterns = [
    path('user/', include('users.urls')),
    path('shop/', include('shop.urls')),
    path('product/', include('products.urls')),
    path('post/', include('post.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Green Space API",
        default_version='v1',
        description = "Green Space API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="21913662@yu.ac.kr"),
        license=openapi.License(name="김지혜"),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_patterns,
)