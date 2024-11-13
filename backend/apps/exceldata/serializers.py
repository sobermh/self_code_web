"""
@author:mh
Code is far away from bug
"""
from rest_framework import serializers

from apps.exceldata.models import *


class MetalDensitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MetalDensityModel
        fields = "__all__"


class MetalCancerRiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetalCancerRiskModel
        fields = "__all__"


class MetalNonCancerRiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetalNonCancerRiskModel
        fields = "__all__"


class MetalAverageAnnualSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetalAverageAnnualModel
        fields = "__all__"


class MetalReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetalReferenceModel
        fields = "__all__"


class SocialEconomySerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialEconomyModel
        fields = "__all__"


class PAHsAverageAnnualSerializer(serializers.ModelSerializer):
    class Meta:
        model = PAHsAverageAnnualModel
        fields = "__all__"


class LandUseRatioSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandUseRatioModel
        fields = "__all__"


class PAHsReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PAHsReferenceModel
        fields = "__all__"


class PAHsCancerRiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = PAHsCancerRiskModel
        fields = "__all__"


class PAHsDensitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PAHsDensityModel
        fields = "__all__"
