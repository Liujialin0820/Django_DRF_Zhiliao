from .views import MerchantViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("merchant", MerchantViewSet, basename="merchant")

urlpatterns = [] + router.urls
