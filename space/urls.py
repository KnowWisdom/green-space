from django.urls import path, include

from space.models import Item, Buy
from .views import *
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'space'

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


urlpatterns = [
    
    path('buy/', BuyList.as_view()),
    path('buy/<int:pk>/', BuyDetail.as_view()),

]

# urlpatterns = format_suffix_patterns(urlpatterns)
