from meituan.models import Merchant
from .serializers import MerchantSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    # 验证用户是否登录成功
    authentication_classes = [BasicAuthentication]
    # 验证登录的用户是否有权限
    permission_classes = [IsAuthenticated]
