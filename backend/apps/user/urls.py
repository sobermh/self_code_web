"""
@author:mh
Code is far away from bug
"""


from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from apps.user.views import UserView,  UserLoginView, UserTokenVerifyView

router = DefaultRouter()
router.register("", UserView, basename="user")  # 用户增删改查

urlpatterns = [
    path("login/", UserLoginView.as_view()),  # 登录
    path("token/verify/", UserTokenVerifyView.as_view())  # 用户token鉴权
]
urlpatterns += router.urls
