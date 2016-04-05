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

class isPermissionNotLogin(BasePermission):
    user_id = 0
    token = ''

    def _post(self, request, key):
        return request.POST.get(key)

    def _get(self, request, key):
        return request.GET.get(key)

    def _put(self, request, key):
        token = request.GET[key]
        return token
    options = {"POST": _post, "GET": _get, "PUT": _put}

    def has_permission(self, request, view):
        request.user_id = 0
        method = request.method
        if method == "DELETE":
            method = "GET"

        # Debug printing
        param = {}
        if method == 'GET':
            for key_name in request.GET:
                param[key_name] = request.GET.get(key_name)
        else:
            for key_name in request.POST:
                param[key_name] = request.POST.get(key_name)

        global log_data
        log_data = {
            'start_time': time.time(),
            'request_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'url_data': {
                'link': request.path,
                'method': method,
                'param': param
            }

        }

        token = self.options[method](self, request, 'token')
        api_key = self.options[method](self, request, 'api_key')
        type = self.options[method](self, request, 'api_type')
        request.token = ''
        if(token != None and token != ""):
            try:
                session = self.model.objects.get(auth_token=token)
                if session:
                    if session.expired > datetime.now():
                        request.user_id = session.customer.id
                        request.token = token
            except ObjectDoesNotExist:
                nothing = 0

        if type==None:
            return 1
        else:
            if type == Constant.SESSION_CUSTOMER_TYPE_DESKTOP:
                customer = request.session.get('customer', None)
                if(customer != None):
                    request.user_id = customer
                return 1
            else:
                return 1

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
