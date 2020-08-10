from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.OrderViewSet)

urlpatterns = [
    path('add/<str:id>/<str:token>/',views.add, name='order.add'),
    path('getOrders/<str:id>/',views.getOrders, name='order.getOrders'),
    path('',include(router.urls)),
]