from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import CreateModelMixin

from rest_framework.viewsets import ModelViewSet

from apps.region.models import RegionModel
from apps.region.serializers import RegionSerializer


class RegionView(ListCreateAPIView):
    """人员信息"""
    queryset = RegionModel.objects.all().order_by("id")  # 模型类queryset
    serializer_class = RegionSerializer
