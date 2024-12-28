from meituan.models import Merchant
from .serializers import MerchantSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .authentications import generate_jwt, JWTAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .permissions import MyPermission

User = get_user_model()


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    # 验证用户是否登录成功 通过一个就可以
    authentication_classes = [JWTAuthentication, BasicAuthentication]
    # 验证登录的用户是否有权限 所有验证都要通过
    permission_classes = [MyPermission]


@api_view(["GET"])
def token_view(request):
    # 随便选一个对象
    token = generate_jwt(User.objects.first())
    return Response({"token": token})
