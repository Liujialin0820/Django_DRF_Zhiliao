from django.urls import path
from .views import merchant, goodsCategory

app_name = "a2"

urlpatterns = [
    path("merchant/", merchant, name="merchant"),
    path("category/", goodsCategory),
]
