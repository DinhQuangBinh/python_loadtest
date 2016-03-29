from rest_framework.response import Response
from rest_framework.generics import (RetrieveAPIView,CreateAPIView)
from nahi.service import *
from test_balance.models.TestBalance import TestBalance
from test_balance.serializers.TestBalanceSerializer import TestBalanceSerializer
#import logging


class GetDataTestBalance(RetrieveAPIView):
    model = TestBalance
    serializer_class = TestBalanceSerializer
    permission_classes = (BasePermission,)
    def get(self, request, *args, **kwargs):
        self.serializer_class.validate_get(self,request.GET)
        offset = int(request.GET['offset'])
        limit = int(request.GET['limit'])
        try:
            data = TestBalance.objects.filter()[offset:limit + offset]
            serializer = self.serializer_class(data,many=True)
            return Response(APIRender.export(self, Constant.API_STATUS_OK, serializer.data, Constant.API_STATUS_MESSAGE_UNSUCCESS))
        except Exception as e:
            return Response(APIRender.export(self, Constant.API_STATUS_UNSUCCESS, "", Constant.API_STATUS_MESSAGE_UNSUCCESS))

class PostDataTestBalance(CreateAPIView):
    serializer_class = TestBalanceSerializer
    permission_classes = (BasePermission,)

    def create(self, request, *args, **kwargs):
        username = 'test'
        password = 'testpassword123456'
        email = 'admin@admin.com'
        try:
            friend = TestBalance.objects.create(username=username,password=password,email=email)
            friend.save()
            serializer = self.serializer_class(friend)
            return Response(APIRender.export(self, Constant.API_STATUS_OK, Constant.API_STATUS_MESSAGE_OK, serializer.data))
        except ObjectDoesNotExist:
            return Response(APIRender.export(self, Constant.API_STATUS_UNSUCCESS, Constant.API_STATUS_MESSAGE_UNSUCCESS, ""))


