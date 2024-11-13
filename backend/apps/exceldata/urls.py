from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.exceldata.views import *

router = DefaultRouter()
router.register("metaldensity", MetalDensityView, basename="metaldensity")

router.register("MetalAverageAnnual", MetalAverageAnnualView, basename="MetalAverageAnnual")
router.register("MetalReference", MetalReferenceView, basename="MetalReference")

router.register("metalcancerrisk", MetalCancerRiskView, basename="pahshealthrisk")
router.register("MetalNonCancerRisk", MetalNonCancerRiskView, basename="MetalNonCancerRisk")

router.register("socialeconomy", SocialEconomyView, basename="socialeconomy")

router.register("PAHsAverageAnnual", PAHsAverageAnnualView, basename="PAHsAverageAnnual")
router.register("LandUseRatio", LandUseRatioView, basename="LandUseRatio")
router.register("PAHsReference", PAHsReferenceView, basename="PAHsReference")
router.register("pahsdensity", PAHsDensityView, basename="pahsdensity")
router.register("PAHsCancerRisk", PAHsCancerRiskView, basename="PAHsCancerRisk")

urlpatterns = [
    path("metaldensity/download/", MetalDensityDownloadView.as_view()),
    path("metalcancerrisk/download/", MetalCancerRiskDownloadView.as_view()),
    path("MetalNonCancerRisk/download/", MetalNonCancerRiskDownloadView.as_view()),
    path("MetalAverageAnnual/download/", MetalAverageAnnualDownloadView.as_view()),
    path("MetalReference/download/", MetalReferenceDownloadView.as_view()),
    path("socialeconomy/download/", SocialEconomyDownloadView.as_view()),
    path("PAHsAverageAnnual/download/", PAHsAverageAnnualDownloadView.as_view()),
    path("LandUseRatio/download/", LandUseRatioDownloadView.as_view()),
    path("PAHsReference/download/", PAHsReferenceDownloadView.as_view()),
    path("PAHsCancerRisk/download/", PAHsCancerRiskDownloadView.as_view()),
    path("pahsdensity/download/", PAHsDensityDownloadView.as_view()),
    # path("token/verify/", UserTokenVerifyView.as_view())  # 用户token鉴权
]
urlpatterns += router.urls
