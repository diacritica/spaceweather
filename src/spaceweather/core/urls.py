from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'protonflux', views.ProtonfluxViewSet)
router.register(r'ptypes', views.PtypeViewSet)
