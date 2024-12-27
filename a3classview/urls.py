from django.urls import path
from .views import MerchantView,MerchantDetailView

app_name = "classview"
urlpatterns = [
    path("merchant/", MerchantView.as_view()),
    path("merchant/<int:pk>/", MerchantDetailView.as_view()),
]
