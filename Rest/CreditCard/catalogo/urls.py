from rest_framework import routers
from .views import ProductoViewSet, SituacionAgenViewSet, LugarAperturaViewSet, LocalidadViewSet, StatusFinalViewSet, UniversidadViewSet, CausarechazoViewSet

router = routers.SimpleRouter()
router.register(r'producto', ProductoViewSet, 'producto')
router.register(r'situacionagen', SituacionAgenViewSet, 'situacionagen')
router.register(r'lugarapertura', LugarAperturaViewSet, 'lugarapertura')
router.register(r'localidad', LocalidadViewSet, 'localidad')
router.register(r'statusfinal', StatusFinalViewSet, 'statusfinal')
router.register(r'universidad', UniversidadViewSet, 'universidad')
router.register(r'causarechazo', CausarechazoViewSet, 'causarechazo')
urlpatterns = router.urls

