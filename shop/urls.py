from django.urls import path, include

from shop.models import Item, Buy
from .views import *
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'shop'

# Item 목록 보여주기
item_list = ItemViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

# Item 세부사항 보여주기 / 수정 / 삭제
item_detail = ItemViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'delete' : 'destroy'
})

badge_list = BadgeViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

badge_detail = BadgeViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'delete' : 'destroy'
})


urlpatterns = [
    path('items/', item_list),
    path('items/<int:pk>', item_detail),
    path('badges/', badge_list),
    path('badges/<int:pk>', badge_detail),
    path('buy/', BuyList.as_view()),
    path('space/', SpaceView.as_view()),

]

# urlpatterns = format_suffix_patterns(urlpatterns)
