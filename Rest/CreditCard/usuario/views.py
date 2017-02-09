from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
# Create your views here.

class UsuarioViews(APIView):
    def get(self, request):
        # return Response({'hola':'mundo'})
        return JsonResponse({'status':status.HTTP_204_NO_CONTENT})
