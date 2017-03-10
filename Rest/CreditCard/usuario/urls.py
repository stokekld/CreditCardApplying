from django.conf.urls import url, include

from rest_framework import routers
# from .views import UsuarioViews, UsuarioAuth
from .views import UsuarioViewSet

router = routers.SimpleRouter()
router.register(r'usuarios', UsuarioViewSet, 'usuarios')
# urlpatterns = router.urls

urlpatterns = [
    # url(r'^$', UsuarioViews.as_view(), name='usuarios'),
    # url(r'^/auth$', UsuarioAuth.as_view(), name='auth'),
    url(r'usuarios', include(router.urls)),
]

