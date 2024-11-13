"""
@author:mh
Code is far away from bug
"""
import re

from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.user.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    """用户表"""

    class Meta:
        model = UserModel
        fields = "__all__"

        extra_kwargs = {  # 修改字段选项
            'password': {
                'write_only': True,
                'min_length': 6,
                'max_length': 20,
                'error_messages': {  # 自定义校验出错后的错误信息提示
                    'min_length': '仅允许6-20个字符的密码',
                    'max_length': '仅允许6-20个字符的密码',
                }
            },

        }

    def validate_password(self, value):
        """单独验证密码"""
        return make_password(value)  # 返回加密的密码


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """登录token校验"""

    @classmethod
    def get_token(cls, user):
        """自定义令牌中的内容"""
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims

        # 是否是超级管理员
        token['is_superuser'] = user.is_superuser
        # print(user)
        return token

    def validate(self, attrs):
        """自定义返回值"""
        data = super().validate(attrs)

        # refresh = self.get_token(self.user)
        del data['refresh']
        data["token"] = data.pop("access")
        # # data['access'] = str(refresh.access_token)
        data['username'] = self.user.username
        data["id"] = self.user.id
        # data['userid'] = self.user.id
        return data

