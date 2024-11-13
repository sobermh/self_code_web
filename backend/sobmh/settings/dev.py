from .common import *

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

# MEDIA_URL = "http://hxwebapi.hxsensors.com:9024/media/"  # 文件、图片的URI前缀， 比如 http://127.0.0.1:8080/media/cover/xxx.jpg


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'psl_visualization',
        # create database If Not Exists psl_visualization default charset utf8 collate utf8mb4_general_ci;
        'USER': 'pslremote',
        'PASSWORD': 'pslremote',
        'HOST': '47.120.5.62',
        'POST': '3306',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8mb4_general_ci'}
    }
}

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = "UTC"
# USE_I18N = True
# USE_TZ = True


LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True