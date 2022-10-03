from django.urls import path

from space.models import Item, Buy
from .views import *
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
    path('items/', item_list),
    path('items/<int:pk>/', item_detail),
    path('buy/', BuyView.as_view()),
    # path('buy/<int:pk>/', buy_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
