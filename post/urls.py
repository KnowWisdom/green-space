from django.urls import path, include

from shop.models import Item, Buy
from .views import *
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'post'

urlpatterns = [
    path('', PostListView.as_view()),
    path('<int:pk>', PostDetailView.as_view(), name='post-detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
