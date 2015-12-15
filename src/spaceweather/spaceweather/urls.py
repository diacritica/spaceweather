from django.conf.urls import include, url

from rest_framework.authtoken.views import obtain_auth_token

from core.urls import router
from core.views import servefiles


urlpatterns = [
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
    url(r'^api/imagechannels/images/(?P<file>(.+))$', servefiles),
]
