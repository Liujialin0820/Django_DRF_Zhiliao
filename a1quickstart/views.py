from rest_framework import viewsets
from meituan.models import Merchant
from .serializers import MerchantSerializer


# 这个试图包含了增删改查操作
class MerchantViewset(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
