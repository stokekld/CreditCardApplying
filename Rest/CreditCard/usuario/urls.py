from django.conf.urls import url, include
from rest_framework import routers
from .views import UsuarioViewSet

router = routers.SimpleRouter()
router.register(r'usuarios', UsuarioViewSet, 'usuarios')
urlpatterns = router.urls


