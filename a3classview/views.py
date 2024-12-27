###########################################################################
#################################APIView###################################
###########################################################################

# from rest_framework.views import APIView
# from meituan.models import Merchant
# from django.http import Http404
# from rest_framework.response import Response
# from .serializers import MerchantSerializer
# from rest_framework import status


# class MerchantView(APIView):
#     def get_object(self, pk):
#         try:
#             return Merchant.objects.get(pk=pk)
#         except Merchant.DoesNotExist:
#             raise Http404

#     def get(self, request, pk=None):
#         if pk:
#             merchant = self.get_object(pk)
#             serializer = MerchantSerializer(merchant)
#             return Response(serializer.data)
#         else:
#             queryset = Merchant.objects.all()
#             serializer = MerchantSerializer(instance=queryset, many=True)
#             return Response(serializer.data)

#     def put(self, request, pk):
#         merchant = self.get_object(pk)
#         serializer = MerchantSerializer(merchant, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         merchant = self.get_object(pk)
#         merchant.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


###########################################################################
#################################Mixin#####################################
###########################################################################

# from meituan.models import Merchant
# from django.http import Http404
# from rest_framework.response import Response
# from .serializers import MerchantSerializer
# from rest_framework import status, generics, mixins


# class MerchantView(
#     generics.GenericAPIView,
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.CreateModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
# ):
#     queryset = Merchant.objects.all()
#     serializer_class = MerchantSerializer

#     def get(self, request, pk=None):
#         if pk:
#             return self.retrieve(request)
#         return self.list(request)

#     def post(self, request):
#         # 如果要更改添加逻辑, 重写perform_create方法
#         return self.create(request)

#     def put(self, request, pk):
#         return self.update(request, pk)

#     def delete(self, request, pk):
#         return self.destroy(request, pk)

###########################################################################
#################################APIView###################################
###########################################################################

from meituan.models import Merchant
from .serializers import MerchantSerializer
from rest_framework import generics


class MerchantView(
    generics.ListAPIView,
    generics.CreateAPIView,
):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer


class MerchantDetailView(
    generics.DestroyAPIView,
    generics.UpdateAPIView,
    generics.RetrieveAPIView,
):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    # lookup_field='name'
    # URL处要一并修改
    # path("merchant/<str:name>/", MerchantDetailView.as_view()),
