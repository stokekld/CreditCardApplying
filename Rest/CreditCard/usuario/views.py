from rest_framework.views import APIView
from app.response import Response
from rest_framework import status

from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViews(APIView):
    def get(self, request):
        return Response()

    def post(self, request):
        print request.data
        return Response(data={'hola': 1}, status=400)

# class UsuarioAuth(APIView):
class UsuarioAuth(APIView):

    serializer = UsuarioSerializer
    def dict(self, data):

        newDict = {}

        for key in data:
            newDict[ UsuarioSerializer().get_fields()[ key ].source ] = data[key]

        return newDict

    def post(self, request):

        # print request.data

        query = self.dict(request.data)

        usuario = Usuario.objects.get(**query);

        print usuario

        return Response(data={'hola': 1}, status=400)

