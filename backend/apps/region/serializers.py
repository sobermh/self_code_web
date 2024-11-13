"""
@author:mh
Code is far away from bug
"""
from rest_framework import serializers

from apps.region.models import RegionModel


class RegionSerializer(serializers.ModelSerializer):
    """用户表"""

    class Meta:
        model = RegionModel
        fields = "__all__"
        #
        # extra_kwargs = {  # 修改字段选项
        #     'password': {
        #         'write_only': True,
        #         'min_length': 6,
        #         'max_length': 20,
        #         'error_messages': {  # 自定义校验出错后的错误信息提示
        #             'min_length': '仅允许6-20个字符的密码',
        #             'max_length': '仅允许6-20个字符的密码',
        #         }
        #     },
        #
        # }
    #
    # def validate_password(self, value):
    #     """单独验证密码"""
    #     return make_password(value)  # 返回加密的密码
