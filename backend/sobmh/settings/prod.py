"""
@author:maohui
"""

from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ----------------------- 动态文件配置------------------------------------------------
# MEDIA_URL = "https://hxwebapi.well-healthcare.com/media/"  # 文件、图片的URI前缀， 比如 http://127.0.0.1:8080/media/cover/xxx.jpg
# print(MEDIA_ROOT)


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

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

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True
