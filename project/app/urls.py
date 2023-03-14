from django.urls import path, include
from .views import ViewCategory, ViewPets, ViewStatus, ViewType, ViewOrderStatus, ViewOrder
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'types', ViewType)
router.register(r'pets', ViewPets)
router.register(r'categoryes', ViewCategory)
router.register(r'statusespet', ViewStatus)
router.register(r'statusesorder', ViewOrderStatus)
router.register(r'orders', ViewOrder)



urlpatterns = [
    path('', include(router.urls)),
]
