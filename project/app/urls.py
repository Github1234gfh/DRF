from django.urls import path, include
from .views import ViewProduct, ViewBin
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'products', ViewProduct)
router.register(r'bin', ViewBin)

urlpatterns = [
    path('', include(router.urls))
]