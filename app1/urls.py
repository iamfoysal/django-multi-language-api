from django.urls import path, include
from .views import PostViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'api', PostViewset, basename='api')
urlpatterns = router.urls
