from meituan.models import Merchant
from .serializers import MerchantSerializer
from rest_framework import generics, viewsets


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer