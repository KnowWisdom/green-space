from django.urls import path

from products.models import Product
from .views import ProductViewSet
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'products'

# Product 목록 보여주기
product_list = ProductViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

# Product 세부사항 보여주기 / 수정 / 삭제
product_detail = ProductViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'delete' : 'destroy'
}) 

urlpatterns = [
    path('', product_list),
    path('<int:pk>/', product_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
