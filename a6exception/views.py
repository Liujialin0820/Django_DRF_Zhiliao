from meituan.models import Merchant
from .serializers import MerchantSerializer
from rest_framework import viewsets
from rest_framework.decorators import action


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

    @action(["GET"], detail=False)
    def my(self, request):
        Merchant.objects.update(id=1)
        return {}
