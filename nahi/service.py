__author__ = 'tienmn'
from datetime import datetime
from rest_framework import generics
from django.core.exceptions import ObjectDoesNotExist
from nahi.constants import Constant
from django.utils import timezone
import time, logging, json
from nahi.config import Config

class APIRender():
    def export(self, status, message, data):
        if Config.DEBUG_API_PROFILE:
            logger_api = logging.getLogger('api_profile')
            try:
                global log_data
                if log_data:
                    logger_api.info('\nRequested time: %r' % (log_data.get('request_time')))
                    logger_api.info('Response time: %r msecs' % ((time.time() - log_data.get('start_time'))*1000))
                    logger_api.info('Requested URL: %r' % (log_data.get('url_data').get('link')))
                    logger_api.info('Method: %r' % (log_data.get('url_data').get('method')))
                    logger_api.info('Parameters:')
                    logger_api.info(json.dumps(log_data.get('url_data').get('param'), indent=4))
                    logger_api.info('Response information:')
                    logger_api.info('\tStatus: %r' % (status))
                    logger_api.info('\tMessage: %r' % (message))
            except Exception as error:
                print (error)
        return {Constant.API_STATUS: status, Constant.API_MESSAGE: message, Constant.API_RESULT: data}


class BasePermission(object):
    """
    A base class from which all permission classes should inherit.
    """
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True

class ListCreateAPIViewBase(generics.ListCreateAPIView):
    def begin(self):
        return ""
    
class ListAPIViewBase(generics.ListAPIView):
    def begin(self):
        return ""

class CreateAPIViewBase(generics.CreateAPIView):
    def begin(self):
        return ""

class RetrieveAPIViewBase(generics.RetrieveAPIView):
    def begin(self):
        return ""

class DestroyAPIViewBase(generics.DestroyAPIView):
    def begin(self):
        return ""
