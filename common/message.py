'''
Created on Jun 30, 2015

@author: lietqn
'''

class CommonMessage():
    PARAMETTER_IS_MISSING = {'code':100, 'message':'Parameter is missing'}
    #
    USER_IS_NOT_EXISTING = {'code':200, 'message':'User is not existing'}
    USER_FAVOURITED_OBJECT = {'code':201, 'message':'User has been favourited this object'}
    USER_FAVOURITE_OBJECT_SUCCESS = {'code':202, 'message':'User favourite object successfully'}
    USER_UNFAVOURITED_OBJECT = {'code':203, 'message':'User has not been favourited this object'}
    USER_UNFAVOURITE_OBJECT_SUCCESS = {'code':204, 'message':'User unfavourite object successfully'}
            
