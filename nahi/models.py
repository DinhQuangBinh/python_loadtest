__author__ = 'tienmn'
from django.db import models
class customFloatField(models.Field):
    def db_type(self, connection):
        return 'float'