# from rest_framework import serializers
# from meituan.models import Merchant


# 1. 序列化数据 ORM->Json
# 2. 验证表单数据
# 3. 创建修改数据
# class MerchantSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=200, required=True)
#     logo = serializers.CharField(max_length=200, required=True)
#     address = serializers.CharField(max_length=200, required=True)
#     notice = serializers.CharField(max_length=200, required=True)
#     up_send = serializers.DecimalField(required=False, max_digits=6, decimal_places=2)
#     lon = serializers.FloatField(required=True)
#     lat = serializers.FloatField(required=True)

#     # 验证功能
#     def validate(self, attrs):
#         return super().validate(attrs)

#     # 创建修改数据功能
#     def create(self, validated_data):
#         return Merchant.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.notice = validated_data.get("notice", instance.notice)
#         instance.logo = validated_data.get("logo", instance.logo)
#         instance.address = validated_data.get("address", instance.address)
#         instance.up_send = validated_data.get("up_send", instance.up_send)
#         instance.lon = validated_data.get("lon", instance.lon)
#         instance.lat = validated_data.get("lat", instance.lat)
#         instance.save()
#         return instance


########################################################################################
from rest_framework import serializers
from meituan.models import Merchant, GoodsCategory, Goods


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"


class GoodsCategorySerializer(serializers.ModelSerializer):
    merchant = MerchantSerializer(read_only=True)
    merchant_id = serializers.IntegerField(write_only=True)
    goods_list = GoodsSerializer(many=True, read_only=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"

    def validate_merchant_id(self, value):
        if not Merchant.objects.filter(pk=value).exists():
            raise serializers.ValidationError("商家不存在!")
        return value

    def create(self, validated_data):
        merchant_id = validated_data.get("merchant_id")
        merchant = Merchant.objects.get(pk=merchant_id)
        cateogry = GoodsCategory.objects.create(**validated_data, merchant=merchant)
        return cateogry
