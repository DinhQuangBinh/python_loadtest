'''
Created on Jun 30, 2015

@author: lietqn
'''

from nahi.service import APIRender, CreateAPIViewBase, RetrieveAPIViewBase
from rest_framework.response import Response
from common.convert import CommonConvert

class CommonApiStatus():
    class Ok():        
        code = 1000
        message = 'OK'
        
    class Error():
        code = 1001
        message = 'ERROR'
        
    class Message():
        PARAMETTER_IS_MISSING = {'code':100, 'message':'Parameter is missing'}
            

class CommonApi():    
    
    def Error(self,result):
        return Response(APIRender.export(self, CommonApiStatus.Error.code, CommonApiStatus.Error.message,result))
    
    def Success(self,result):
        return Response(APIRender.export(self, CommonApiStatus.Ok.code, CommonApiStatus.Ok.message,result))
    
    def parameter_missing(self, field):
        CommonApiStatus.Message.PARAMETTER_IS_MISSING['field'] = field
        return CommonApi.Error(self, CommonApiStatus.Message.PARAMETTER_IS_MISSING)

class CommonApiAction():
    arr_input = {} 
    request = None
    
    def action(self, request, *args, **kwargs):
        return CommonApi.Error(self, 'You must override action method')
    
    def map_input(self,name1, name2):
        self.arr_input[name1] = name2
        
    def get_input_name(self, name):
        try:
            return self.arr_input[name]
        except:
            return name
        
    def get_input_value(self, name, func, default):  
        name = self.get_input_name(name)   
        value = self.request.data.get(name)
        return CommonConvert.get(self, func, value, default)

class CommonApiPostView(CreateAPIViewBase, CommonApiAction):
        
    def create(self, request, *args, **kwargs):
        self.request = request
        return self.action(request, *args, **kwargs)
    
    def get_input_value(self, name, func, default):  
        name = self.get_input_name(name)  
        try: 
            value = self.request.POST[name]
            return func(value)
        except:
            return default
    
class CommonApiGetView(RetrieveAPIViewBase, CommonApiAction):
        
    def retrieve(self, request, *args, **kwargs):        
        self.request = request
        return self.action(request, *args, **kwargs)
    
    def get_input_value(self, name, func, default):  
        name = self.get_input_name(name)  
        try: 
            value = self.request.GET[name]
            return func(value)
        except:
            return default