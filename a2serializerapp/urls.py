from django.urls import path
from .views import merchant

app_name = "a2"

urlpatterns = [path("merchant/", merchant, name="merchant")]
