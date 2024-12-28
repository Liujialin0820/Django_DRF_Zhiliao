from meituan.models import Merchant
from .serializers import MerchantSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .authentications import generate_jwt
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view

User = get_user_model()


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    # 验证用户是否登录成功
    authentication_classes = [BasicAuthentication]
    # 验证登录的用户是否有权限
    permission_classes = [IsAuthenticated]


@api_view(["GET"])
def token_view(request):
    # 随便选一个对象
    token = generate_jwt(User.objects.first())
    return Response({"token": token})
