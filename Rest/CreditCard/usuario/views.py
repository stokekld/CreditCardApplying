from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from app.response import Response
from app.tools import translate
from app.token import Token
from app.request import Request
from rest_framework import status

from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViews(APIView):
    def get(self, request):
        return Response()

    def post(self, request):
        return Response(data={'hola': 1}, status=400)

# class UsuarioAuth(APIView):
class UsuarioAuth(APIView):

    def post(self, request):

        try:
            query = translate(UsuarioSerializer, Request(request).data)
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

