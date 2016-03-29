__author__ = 'tienmn'
from rest_framework.views import exception_handler
from nahi.constants import Constant
import tempfile
import uuid
import urllib
import base64

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    # Now add the HTTP status code to the response.
    if response is not None and response.status_code == 401:
        response.data[Constant.API_STATUS] = Constant.API_STATUS_TOKENEXPIRED
        response.data[Constant.API_MESSAGE] = Constant.API_STATUS_MESSAGE_TOKENEXPIRED
        response.data['code'] = response.status_code
         
    return response



    
