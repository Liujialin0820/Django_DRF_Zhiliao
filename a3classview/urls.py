from django.urls import path
from .views import MerchantView

app_name = "classview"
urlpatterns = [
    path("merchant/", MerchantView.as_view()),
    path("merchant/<int:pk>/", MerchantView.as_view()),
]
