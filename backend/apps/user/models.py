
# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class UserModel(BaseModel, AbstractUser):
    """
    用户表
    notes:需要修改setting.py的AUTH_USER_MODEL配置
    """

    # email = models.EmailField("邮箱", max_length=255, blank=True, null=True)
    # id_in_oa = models.IntegerField(verbose_name="在oa中的id",null=True,blank=True)
    # name = models.CharField("真实姓名", max_length=30, blank=True, null=True)
    # phone = models.CharField("手机号", max_length=20, blank=True, null=True)
    username = models.CharField("员工编号", max_length=32, unique=True)
    # dept = models.ForeignKey(Department, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='部门')
    # roles = models.ManyToManyField(Role, blank=True, related_name="user_role", verbose_name="角色")
    # position = models.CharField(max_length=32, blank=True, null=True, verbose_name="职位")
    # （直接上级拥有下级的所有查看权限）
    # superior = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="上级用户")

    class Meta:
        # indexes = [
        #     models.Index(fields=["number"], name="username_idx"),
        #     models.Index(fields=["id_in_oa"], name="id_in_oa_idx"),
        # ]

        db_table = "user"
#
#     def role_detail(self):
#         """直接序列化role表的id、name"""
#         # return self.s_achievement.all() 不行，模型对象不是json
#         # return self.s_achievement.values(）
#         return self.roles.values("id", "name")
#
#     @property  # 可写可不写
#     def dept_detail(self):
#         """直接序列化dept表的id、name"""
#         return self.dept.id, self.dept.name
#
#     def superior_detail(self):
#         """直接序列化上级"""
#         if self.superior is None:
#             return None
#         return self.superior.id, self.superior.realname
