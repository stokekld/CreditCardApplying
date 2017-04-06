from rest_framework import viewsets
from rest_framework.decorators import list_route
from django.core.exceptions import ObjectDoesNotExist
import hashlib

from app.response import Response
from app.tools import translate
from app.token import Token
from app.request import Request
from rest_framework import status

from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ViewSet):

    @list_route(methods=['post'])
    def auth(self, request):
        try:
            credentials = Request(request).data
            credentials["password"] = hashlib.md5(credentials["password"]).hexdigest()
            query = translate(UsuarioSerializer, credentials)
        except KeyError:
            return Response({}, status.HTTP_400_BAD_REQUEST, "Envio erroneo de parametros")

        try:
            usuarios = Usuario.objects.filter(**query)

            if usuarios.count() is not 1:
                raise ObjectDoesNotExist

        except ObjectDoesNotExist:
            return Response({}, status.HTTP_404_NOT_FOUND, "No se encontro el usuario")

        token = Token.getToken(UsuarioSerializer(usuarios[0]).data)

        return Response({'token': token})


