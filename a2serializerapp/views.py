from .serializers import MerchantSerializer, GoodsCategorySerializer
from rest_framework import status
from meituan.models import Merchant, GoodsCategory
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# 如果要使用Response 方法view 就要加上装饰器
# 如果是类view 就要继承apiview 才可以使用
@api_view(["GET", "POST"]) 
def merchant(request):
    if request.method == "GET":
        queryset = Merchant.objects.all()
        serializer = MerchantSerializer(instance=queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        serializer = MerchantSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def goodsCategory(request):

    if request.method == "GET":
        queryset = GoodsCategory.objects.all()
        serializer = GoodsCategorySerializer(instance=queryset, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    else:
        serializer = GoodsCategorySerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)
