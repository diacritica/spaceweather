from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'protonflux', views.ProtonfluxViewSet)
router.register(r'electronflux', views.ElectronfluxViewSet)
router.register(r'xrayflux', views.XrayfluxViewSet)
router.register(r'sunspot', views.SunspotViewSet)
router.register(r'ptypes', views.PtypeViewSet)
router.register(r'etypes', views.EtypeViewSet)
router.register(r'xtypes', views.XtypeViewSet)
router.register(r'sunspottypes', views.SunspottypeViewSet)
router.register(r'sunspotregion', views.SunspotregionViewSet)
router.register(r'alerttypes', views.AlerttypeViewSet)
router.register(r'alerts', views.AlertViewSet)
router.register(r'channeltypes', views.ChanneltypeViewSet)
router.register(r'imagechannels', views.ImagechannelViewSet)
