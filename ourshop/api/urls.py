from django.urls import re_path as url
from django.urls import include
from .views import CategoryViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("category", CategoryViewSet, basename="category")
router.register("product", ProductViewSet, basename="product")


urlpatterns = [
    url('', include(router.urls))
    ]