class Config():

    
    DATABASES = {
        'default': {
            'NAME': 'test_balance',
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'test_balance',
            'PASSWORD': 'Aa123456@',
            'HOST': '202.43.110.121',
            'PORT': '3306',
        },

        'test_balance': {
            'NAME': 'test_balance',
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'test_balance',
            'PASSWORD': 'Aa123456@',
            'HOST': '202.43.110.121',
            'PORT': '3306',
        },
    }

    XS_SHARING_ALLOWED_ORIGINS = ['http://127.0.0.1', 'http://localhost']
    # Media upload localhost
    MEDIA_ROOT = 'media'

    # Folder Content Center
    MEDIA_FOLDER_CONTENTCENTER_CONTENT = 'media/upload/temp'
    MEDIA_FOLDER_CONTENTCENTER_ROOT = 'media/upload'

    DATABASE_ROUTERS = ['test_balance.routers.TBRouter']

    TIME_ZONE = 'Asia/Saigon'

    DEBUG_API_PROFILE = True
    


