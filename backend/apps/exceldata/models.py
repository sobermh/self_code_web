from django.db import models


# Create your models here.

class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class MetalDensityModel(BaseModel):
    year = models.IntegerField(null=True)
    city = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=50, null=True)

    # Cd = models.FloatField(null=True)
    # Pd = models.FloatField(null=True)
    # Cu = models.FloatField(null=True)
    # Zn = models.FloatField(null=True)
    # Ni = models.FloatField(null=True)
    # Cr = models.FloatField(null=True)
    # As = models.FloatField(null=True)
    # Hg = models.FloatField(null=True)
    # HM = models.FloatField(null=True)

    class Meta:
        db_table = "metal_density"


class MetalCancerRiskModel(BaseModel):
    year = models.IntegerField(null=True)
    city = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    value = models.DecimalField(max_digits=25, decimal_places=20, null=True)
    is_adult = models.BooleanField(null=True, default=False)

    class Meta:
        db_table = "metal_cancer_risk"


class MetalNonCancerRiskModel(BaseModel):
    year = models.IntegerField(null=True)
    city = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    value = models.DecimalField(max_digits=25, decimal_places=20, null=True)
    is_adult = models.BooleanField(null=True, default=False)

    class Meta:
        db_table = "metal_non_cancer_risk"


class MetalAverageAnnualModel(BaseModel):
    year = models.IntegerField(null=True)
    type = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = "metal_average_annual"


class MetalReferenceModel(BaseModel):
    type = models.CharField(max_length=50, null=True)
    reference_number = models.IntegerField(null=True)

    class Meta:
        db_table = "metal_reference"


class SocialEconomyModel(BaseModel):
    year = models.IntegerField(null=True)
    # province = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    factors = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = "social_economy"


class PAHsAverageAnnualModel(BaseModel):
    year = models.IntegerField(null=True)
    type = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = "PAHs_average_annual"


class LandUseRatioModel(BaseModel):
    type = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = "land_use_ratio"


class PAHsReferenceModel(BaseModel):
    year = models.IntegerField(null=True)
    reference_number = models.IntegerField(null=True)

    class Meta:
        db_table = "PAHs_reference"


class PAHsCancerRiskModel(BaseModel):
    year = models.IntegerField(null=True)
    city = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    value = models.DecimalField(max_digits=25, decimal_places=20, null=True)
    is_adult = models.BooleanField(null=True, default=False)

    class Meta:
        db_table = "PAHs_cancer_risk"


class PAHsDensityModel(BaseModel):
    year = models.IntegerField(null=True)
    city = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = "PAHs_density"
