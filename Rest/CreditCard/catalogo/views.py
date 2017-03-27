from rest_framework import viewsets
from app.response import Response

from .models import Producto, Situacionagen, Lugarapertura, Localidad, Statusfinal, Universidad, Causarechazo
from .serializers import ProductoSerializer, SituacionagenSerializer, LugaraperturaSerializer, LocalidadSerializer, StatusfinalSerializer, UniversidadSerializer, CausarechazoSerializer

class ProductoViewSet(viewsets.ViewSet):

    def list(self, request):
        producto = ProductoSerializer( Producto.objects.all(), many=True )
        return Response(producto.data)

class SituacionAgenViewSet(viewsets.ViewSet):

    def list(self, request):
        situacionagen = SituacionagenSerializer( Situacionagen.objects.all(), many=True )
        return Response(situacionagen.data)

class LugarAperturaViewSet(viewsets.ViewSet):

    def list(self, request):
        lugarap = LugaraperturaSerializer( Lugarapertura.objects.all(), many=True )
        return Response(lugarap.data)

class LocalidadViewSet(viewsets.ViewSet):

    def list(self, request):
        localidad = LocalidadSerializer( Localidad.objects.all(), many=True )
        return Response(localidad.data)

class StatusFinalViewSet(viewsets.ViewSet):

    def list(self, request):
        statusfin = StatusfinalSerializer( Statusfinal.objects.all(), many=True )
        return Response(statusfin.data)

class UniversidadViewSet(viewsets.ViewSet):

    def list(self, request):
        universidad = UniversidadSerializer( Universidad.objects.all(), many=True )
        return Response(universidad.data)


class CausarechazoViewSet(viewsets.ViewSet):

    def list(self, request):
        causa = CausarechazoSerializer( Causarechazo.objects.all(), many=True )
        return Response(causa.data)
