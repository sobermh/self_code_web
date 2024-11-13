from _decimal import InvalidOperation
from decimal import Decimal

import django_filters
from django.db.models import Q
from django_filters import filters

from apps.exceldata.models import *


class MetalDensityFilter(django_filters.FilterSet):
    year = filters.NumberFilter(field_name="year", lookup_expr='exact')
    min_year = filters.NumberFilter(field_name="year", lookup_expr='gte')
    max_year = filters.NumberFilter(field_name="year", lookup_expr='lte')
    city = filters.CharFilter(lookup_expr="contains")
    value = filters.NumberFilter(field_name="value", lookup_expr='exact')
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')
    type = filters.CharFilter(lookup_expr="exact")

    class Meta:
        model = MetalDensityModel
        fields = "__all__"


class MetalAverageAnnualFilter(django_filters.FilterSet):
    year = filters.NumberFilter(field_name="year", lookup_expr='exact')
    min_year = filters.NumberFilter(field_name="year", lookup_expr='gte')
    max_year = filters.NumberFilter(field_name="year", lookup_expr='lte')
    value = filters.NumberFilter(field_name="value", lookup_expr='exact')
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')
    type = filters.CharFilter(lookup_expr="exact")

    class Meta:
        model = MetalAverageAnnualModel
        fields = "__all__"


class MetalReferenceFilter(django_filters.FilterSet):
    type = filters.CharFilter(lookup_expr="exact")
    reference_number = filters.NumberFilter(field_name="reference_number", lookup_expr='exact')
    min_reference_number = filters.NumberFilter(field_name="reference_number", lookup_expr='gte')
    max_reference_number = filters.NumberFilter(field_name="reference_number", lookup_expr='lte')

    class Meta:
        model = MetalReferenceModel
        fields = "__all__"


class SocialEconomyFilter(django_filters.FilterSet):
    year = filters.NumberFilter(field_name="year", lookup_expr='exact')
    min_year = filters.NumberFilter(field_name="year", lookup_expr='gte')
    max_year = filters.NumberFilter(field_name="year", lookup_expr='lte')
    city = filters.CharFilter(lookup_expr="contains")
    # province = filters.CharFilter(lookup_expr="exact")
    factors = filters.CharFilter(lookup_expr="exact")
    type = filters.CharFilter(lookup_expr="exact")
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')

    class Meta:
        model = SocialEconomyModel
        fields = "__all__"


class MetalCancerRiskFilter(django_filters.FilterSet):
    year = filters.NumberFilter(field_name="year", lookup_expr='exact')
    min_year = filters.NumberFilter(field_name="year", lookup_expr='gte')
    max_year = filters.NumberFilter(field_name="year", lookup_expr='lte')
    city = filters.CharFilter(lookup_expr="contains")
    type = filters.CharFilter(lookup_expr="exact")
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')
    beyond_threshold = filters.BooleanFilter(method='filter_beyond_threshold')
    equal_threshold = filters.BooleanFilter(method='filter_equal_threshold')
    is_adult = filters.BooleanFilter(field_name="is_adult", lookup_expr="exact")

    @staticmethod
    def filter_beyond_threshold(queryset, name, value):
        cancer_threshold = Decimal('1e-6')
        if value:  # If beyond_threshold is true
            return queryset.filter(Q(value__gt=cancer_threshold))
        else:  # If beyond_threshold is false
            return queryset.filter(Q(value__lt=cancer_threshold))

    @staticmethod
    def filter_equal_threshold(queryset, name, value):
        cancer_threshold = Decimal('1e-6')
        if value:
            return queryset.filter(Q(value=cancer_threshold))
        else:
            return queryset.filter(~Q(value=cancer_threshold))

    class Meta:
        model = MetalCancerRiskModel
        fields = "__all__"


class MetalNonCancerRiskFilter(django_filters.FilterSet):
    year = filters.NumberFilter(field_name="year", lookup_expr='exact')
    min_year = filters.NumberFilter(field_name="year", lookup_expr='gte')
    max_year = filters.NumberFilter(field_name="year", lookup_expr='lte')
    city = filters.CharFilter(lookup_expr="contains")
    type = filters.CharFilter(lookup_expr="exact")
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')
    beyond_threshold = filters.BooleanFilter(method='filter_beyond_threshold')
    equal_threshold = filters.BooleanFilter(method='filter_equal_threshold')
    is_adult = filters.BooleanFilter(field_name="is_adult", lookup_expr="exact")

    @staticmethod
    def filter_beyond_threshold(queryset, name, value):
        non_cancer_threshold = Decimal('1')
        if value:  # If beyond_threshold is true
            return queryset.filter(Q(value__lt=non_cancer_threshold))
        else:  # If beyond_threshold is false
            return queryset.filter(Q(value__gte=non_cancer_threshold))

    @staticmethod
    def filter_equal_threshold(queryset, name, value):
        non_cancer_threshold = Decimal('1')
        if value:
            return queryset.filter(Q(value=non_cancer_threshold))
        else:
            return queryset.filter(~Q(value=non_cancer_threshold))

    class Meta:
        model = MetalNonCancerRiskModel
        fields = "__all__"


class PAHsAverageAnnualFilter(django_filters.FilterSet):
    year = filters.NumberFilter(field_name="year", lookup_expr='exact')
    min_year = filters.NumberFilter(field_name="year", lookup_expr='gte')
    max_year = filters.NumberFilter(field_name="year", lookup_expr='lte')
    value = filters.NumberFilter(field_name="value", lookup_expr='exact')
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')
    type = filters.CharFilter(lookup_expr="exact")

    class Meta:
        model = PAHsAverageAnnualModel
        fields = "__all__"


class LandUseRatioFilter(django_filters.FilterSet):
    type = filters.CharFilter(lookup_expr="exact")
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')


    class Meta:
        model = LandUseRatioModel
        fields = "__all__"

class PAHsReferenceFilter(django_filters.FilterSet):
    year = filters.NumberFilter(field_name="year", lookup_expr='exact')
    min_year = filters.NumberFilter(field_name="year", lookup_expr='gte')
    max_year = filters.NumberFilter(field_name="year", lookup_expr='lte')
    reference_number = filters.NumberFilter(field_name="reference_number", lookup_expr='exact')
    min_reference_number = filters.NumberFilter(field_name="reference_number", lookup_expr='gte')
    max_reference_number = filters.NumberFilter(field_name="reference_number", lookup_expr='lte')
    class Meta:
        model = PAHsReferenceModel
        fields = "__all__"


class PAHsDensityFilter(django_filters.FilterSet):
    year = filters.NumberFilter(field_name="year", lookup_expr='exact')
    min_year = filters.NumberFilter(field_name="year", lookup_expr='gte')
    max_year = filters.NumberFilter(field_name="year", lookup_expr='lte')
    city = filters.CharFilter(lookup_expr="contains")
    type = filters.CharFilter(lookup_expr="exact")
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')

    class Meta:
        model = PAHsDensityModel
        fields = "__all__"


class PAHsCancerRiskFilter(django_filters.FilterSet):
    year = filters.NumberFilter(field_name="year", lookup_expr='exact')
    min_year = filters.NumberFilter(field_name="year", lookup_expr='gte')
    max_year = filters.NumberFilter(field_name="year", lookup_expr='lte')
    city = filters.CharFilter(lookup_expr="contains")
    type = filters.CharFilter(lookup_expr="exact")
    min_value = filters.NumberFilter(field_name="value", lookup_expr='gte')
    max_value = filters.NumberFilter(field_name="value", lookup_expr='lte')
    beyond_threshold = filters.BooleanFilter(method='filter_beyond_threshold')
    equal_threshold = filters.BooleanFilter(method='filter_threshold')
    is_adult = filters.BooleanFilter(field_name="is_adult", lookup_expr="exact")

    def filter_beyond_threshold(self, queryset, name, value):
        threshold = Decimal('1e-6')
        if value:
            return queryset.filter(Q(value__gt=threshold))
        return queryset.filter(Q(value__lt=threshold))

    def filter_threshold(self, queryset, name, value):
        threshold = Decimal('1e-6')
        if value:
            return queryset.filter(Q(value=threshold))
        return queryset.filter(~Q(value=threshold))

    class Meta:
        model = PAHsCancerRiskModel
        fields = "__all__"
