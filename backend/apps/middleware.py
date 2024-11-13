"""
@author:mh
Code is far away from bug
"""

# 自定义中间件
import threading
import logging

# try:
#     from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
# except ImportError:
#     MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x
from django.utils.deprecation import MiddlewareMixin

_thread_locals = threading.local()


class RequestLogFilter(logging.Filter):
    """
    日志过滤器，将当前请求线程的request信息保存到日志的record上下文
    record带有formater需要的信息。
    """

    def filter(self, record):
        record.ip = getattr(_thread_locals, 'ip', None)
        record.username = getattr(_thread_locals, 'username', None)
        record.http_reffer = getattr(_thread_locals, 'http_reffer', None)
        record.path = getattr(_thread_locals, 'path', None)
        return True


class RequestLogMiddleware(MiddlewareMixin):
    """
    将request的信息记录在当前的请求线程上。
    """

    def process_request(self, request):
        # print(request.META)
        # local.ip = request.META.get('HTTP_X_FORWARDED_FOR', None)
        _thread_locals.ip = request.META.get('REMOTE_ADDR', None)
        _thread_locals.username = ""
        _thread_locals.http_reffer = request.META.get('HTTP_REFERER', None)
        _thread_locals.path = request.META.get('PATH_INFO', None)
