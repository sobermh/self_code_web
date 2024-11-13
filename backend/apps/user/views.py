from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

from apps.user.models import UserModel
from apps.user.serializers import UserSerializer, MyTokenObtainPairSerializer


class CustomJWTAuthentication(JWTAuthentication):
    """
    自定义鉴权逻辑： 自定义一个JWTAuthentication鉴权逻辑,get直接跳过鉴权
    """

    def authenticate(self, request):
        if request.method == "POST":
            return None  # 跳过鉴权
        return super().authenticate(request)


class UserView(ModelViewSet):
    """人员信息"""
    queryset = UserModel.objects.all().order_by("id")  # 模型类queryset
    serializer_class = UserSerializer
    authentication_classes = [CustomJWTAuthentication]

    def get_permissions(self):
        # 人员注册时，不用鉴权和权限
        if self.request.method == "POST":
            return []
        return super().get_permissions()

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True  # Set partial to True
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        request.data["is_active"] = False
        return self.update(request, *args, **kwargs)


class UserLoginView(TokenObtainPairView):
    """用户登录,使用jwt鉴权"""
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        """重写登录，在登陆的时候，将登录时间写入last_login"""
        response = super().post(request, *args, **kwargs)
        # UserModel.objects.filter(id=response.data.get("userid")).update(last_login=datetime.datetime.now())
        # print(response.data.get("token"))
        # # response = HttpResponse('Cookie has been set.')
        # response.set_cookie('token', response.data.get("token"), httponly=True)
        return response


class UserTokenVerifyView(TokenVerifyView):
    """验证jwt_token"""

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
