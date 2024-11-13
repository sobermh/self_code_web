"""
@author:mh
Code is far away from bug
"""
from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.region.views import RegionView
from apps.user.views import UserView

router = DefaultRouter()
# router.register("", UserView, basename="region")  # 用户增删改查

urlpatterns = [
    path("", RegionView.as_view()),  # 区
    # path("token/verify/", UserTokenVerifyView.as_view())  # 用户token鉴权
]
urlpatterns += router.urls
