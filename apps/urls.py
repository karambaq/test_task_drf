from django.urls import path
from .views import AppViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'apps', AppViewSet)
urlpatterns = router.urls