from rest_framework.routers import DefaultRouter
from .views import MerchantViewset

router = DefaultRouter()
router.register("merchant", MerchantViewset, basename="merchant")

app_name = "a1quickstart"
urlpatterns = [] + router.urls
