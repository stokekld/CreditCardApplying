from rest_framework import viewsets
from app.response import Response

class ProductoViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response()

class SituacionAgenViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response()

class LugarAperturaViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response()

class LocalidadViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response()

class StatusFinalViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response()

class UniversidadViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response()


