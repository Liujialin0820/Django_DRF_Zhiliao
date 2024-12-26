from .serializers import MerchantSerializer, GoodsCategorySerializer
from rest_framework import status
from django.views.decorators.http import require_http_methods
from meituan.models import Merchant, GoodsCategory
from django.http import JsonResponse


@require_http_methods(["GET", "POST"])
def merchant(request):
    if request.method == "GET":
        queryset = Merchant.objects.all()
        serializer = MerchantSerializer(instance=queryset, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
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
