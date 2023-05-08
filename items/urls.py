from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('product', views.ProductViewSet)
router.register('category', views.CategoryViewSet)
router.register('order', views.OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('product/search/<str:name>', views.phone_detail, name='phone_detail'),
    path('category/search/<str:name>', views.category_detail, name='category_detail'),
    path('order/search/<str:name>', views.order_detail, name='order_detail'),
]