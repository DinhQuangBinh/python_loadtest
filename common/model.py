'''
Created on Jun 13, 2015

@author: lietqn
'''
from nahi.config import Config

class Database():
    NAME = Config.DATABASES['default'].get('NAME')
    
class DatabaseSocial(Database):
    NAME = Config.DATABASES['default'].get('NAME')
    
class DatabaseSSO(Database):
    NAME = Config.DATABASES['sso'].get('NAME')

class DatabaseStargarden(Database):
    NAME = Config.DATABASES['stargarden'].get('NAME')
    
class DatabaseTDV(Database):
    NAME = Config.DATABASES['tdv'].get('NAME')
    
class DatabaseExecute():
    sql = ''

    def __init__(self,sql):
        self.sql = sql
        
    def execute(self):
        from django.db import connection
        cursor = connection.cursor()
        return cursor.execute(self.sql)
    
class DatabaseQuery():
    sql = ''
    para = {}

    def __init__(self,sql, para=None):
        self.sql = sql
        self.para = para
        
    def get_value(self, func=None, default = None):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute(self.sql, self.para)
        try:
            rows = cursor.fetchall()
            if func == None:
                return rows[0][0]
            return func(rows[0][0])
        except:
            return default
        
    def get_object(self, obj):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute(self.sql, self.para)
        col_names = [desc[0] for desc in cursor.description]
        row = cursor.fetchall()[0]
        m = obj()   
        len_col = len(col_names)
        for i in range(0,len_col):
            setattr(m, col_names[i], row[i])
        return m   
    
    def get_row(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute(self.sql, self.para)
        col_names = [desc[0] for desc in cursor.description]
        row = cursor.fetchall()[0]
        r_d = {} 
        for i in range(0,len(col_names)):                
            r_d[col_names[i]] = row[i]
        return r_d
    
    def get_data(self,model = None):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute(self.sql, self.para)
        #return cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]
        result_list = []
        if model != None:
            for row in cursor.fetchall():
                m = model()   
                len_col = len(col_names)
                for i in range(0,len_col):
                    setattr(m, col_names[i], row[i])
                result_list.append(m)
        else:
            for row in cursor.fetchall():
                r_d = {} 
                for i in range(0,len(col_names)):                
                    r_d[col_names[i]] = row[i]
                result_list.append(r_d)
        return result_list

    def get_export_data(self, model=None, cursor=None):
        col_names = [desc[0] for desc in cursor.description]
        result_list = []
        if model != None:
            for row in cursor.fetchall():
                m = model()
                len_col = len(col_names)
                for i in range(0,len_col):
                    setattr(m, col_names[i], row[i])
                result_list.append(m)
        else:
            for row in cursor.fetchall():
                r_d = {}
                for i in range(0,len(col_names)):
                    r_d[col_names[i]] = row[i]
                result_list.append(r_d)
        return result_list
    
"""
Su dung DatabaseQuery
class GroupSerializer(serializers.ModelSerializer):
    field_moi1 = serializers.IntegerField(source='field_moi')
    class Meta:
        model = NSGroup

class FavouriteGroup(CreateAPIView):
    permission_classes = (isPermission,)    
    
    def create(self, request, *args, **kwargs):       
        sql = "SELECT '123' as field_moi, g.* FROM "+DatabaseSocial.NAME+".ns_groups g"
        q = DatabaseQuery(sql)
        r = q.get_data(NSGroup)
        #r = NSGroup.objects.all()
        s = GroupSerializer(r,many=True)
        return SocialApi.Error(self, s.data)
"""