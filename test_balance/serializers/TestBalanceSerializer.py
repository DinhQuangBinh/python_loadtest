from rest_framework import serializers
from nahi.service import *
from test_balance.models.TestBalance import TestBalance


class TestBalanceSerializer(serializers.ModelSerializer):
    password = serializers.SerializerMethodField(source='password')
    class Meta:
        model = TestBalance
        fields = ('id', 'username', 'password', 'email')

    def get_password(self, obj):
        return str(obj.password)

    def validate_get(self, data):
        if not data.get('offset'):
            raise serializers.ValidationError(APIRender.export(self, Constant.OFFSET, Constant.VALID_CUSTOMER_OFFSET, {Constant.OFFSET: Constant.VALID_CUSTOMER_OFFSET}))
        if not data.get('limit'):
            raise serializers.ValidationError(APIRender.export(self, Constant.LIMIT, Constant.VALID_CUSTOMER_LIMIT, {Constant.LIMIT: Constant.VALID_CUSTOMER_LIMIT}))


