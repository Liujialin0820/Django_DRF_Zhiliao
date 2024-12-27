from rest_framework.views import APIView
from meituan.models import Merchant
from django.http import Http404
from rest_framework.response import Response
from .serializers import MerchantSerializer
from rest_framework import status


class MerchantView(APIView):
    def get_object(self, pk):
        try:
            return Merchant.objects.get(pk=pk)
        except Merchant.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            merchant = self.get_object(pk)
            serializer = MerchantSerializer(merchant)
            return Response(serializer.data)
        else:
            queryset = Merchant.objects.all()
            serializer = MerchantSerializer(instance=queryset, many=True)
            return Response(serializer.data)

    def put(self, request, pk):
        merchant = self.get_object(pk)
        serializer = MerchantSerializer(merchant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        merchant = self.get_object(pk)
        merchant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
