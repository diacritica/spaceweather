from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'protonflux', views.ProtonfluxViewSet)
router.register(r'electronflux', views.ElectronfluxViewSet)
router.register(r'xrayflux', views.XrayfluxViewSet)
router.register(r'ptypes', views.PtypeViewSet)
router.register(r'etypes', views.EtypeViewSet)
router.register(r'xtypes', views.XtypeViewSet)
