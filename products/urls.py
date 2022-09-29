from django.urls import path
from .import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'products'

urlpatterns = [
    path('', views.ProductList.as_view()),
    path('<int:pk>/', views.ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
