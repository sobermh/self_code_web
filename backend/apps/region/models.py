from django.db import models


# Create your models here.


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class RegionModel(BaseModel):
    name = models.CharField(verbose_name="区名", max_length=25, unique=True)

    class Meta:
        db_table = "region"
