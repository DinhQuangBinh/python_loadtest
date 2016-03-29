'''
Created on Jun 5, 2015

@author: lietqn
'''
class CommonConvert():
    # f:function, v: value, d: default, dp: dynamic parametter
    def get(self,f,v,d,dp=False):
        if not v:
            return d
        
        try:
            if dp == True:
                r = f(**v)
            else:
                r = f(v)
            #
            if not r:
                return d
            else:
                return r
        except:
            return d
        
    def to_array(self,obj, include={}, changes={},options={}):        
        re_arr = {}
        if len(include) == 0:
            include={}
            for m in obj.__dict__:
                if m.startswith('_'):
                    continue
                base = obj.__class__.__bases__
                for p in base:                
                    if m in p.__dict__:
                        continue
                include[m] = m        
    
        for m in include:
            try:          
                f = changes[m]
                if callable(f):
                    re_arr[m] = f(obj,options)
                else:
                    re_arr[m] = changes[m]
                continue               
            except:
                pass
             
            method = getattr(obj, m)
            t = method.__class__.__name__
            m = str(m)
            if t == 'NoneType':
                re_arr[m] = None
                continue
            if t == 'int' or t == 'float' or t == 'long' or t == 'complex':
                re_arr[m] = method
                continue
            if t == 'list' or t == 'dict':
                re_arr[m] = method
                continue
            re_arr[m] = str(method)
        return re_arr
    
    def change_array(self, arr, include={}, changes={},options={}):        
        re_arr = []
        len_include = len(include)
        for index in arr:
            t = index.__class__.__name__
            if t == 'dict':
                row = index
            else:
                row = arr[index]
            re_row = {}
            for m in row:
                if len_include > 0 and m not in include:
                    continue
                try: 
                    f = changes[m]
                    if callable(f):
                        re_row[m] = f(row,options)
                    else:
                        re_row[m] = changes[m]
                    continue               
                except:
                    pass
             
                re_row[m] = row[m]
            re_arr.append(re_row)            
        return re_arr