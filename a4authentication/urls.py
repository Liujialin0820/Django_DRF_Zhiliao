# from django.urls import path
# from .views import MerchantView,MerchantDetailView

# app_name = "classview"
# urlpatterns = [
#     path("merchant/", MerchantView.as_view()),
#     path("merchant/<int:pk>/", MerchantDetailView.as_view()),
# ]


from django.urls import path
from .views import MerchantViewSet, token_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("merchant", MerchantViewSet, basename="merchant")

urlpatterns = [
    path("token/", token_view),
] + router.urls
