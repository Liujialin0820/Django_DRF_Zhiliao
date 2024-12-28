from meituan.models import Merchant
from .serializers import MerchantSerializer
from rest_framework import viewsets


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
