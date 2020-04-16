from django.urls import path 
from django.conf.urls import url
from .views import AppViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', AppViewSet)
urlpatterns = router.urls