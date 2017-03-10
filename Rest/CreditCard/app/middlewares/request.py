from django.http import JsonResponse
from rest_framework import status
from app.request import Request as appRequest

class Request(object):
    "Middleware para validar el buen formato del request"
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        try:
            appRequest(request)
        except Exception as e:
            return JsonResponse({'error': "El contenido no es json"}, status=status.HTTP_400_BAD_REQUEST)

        response = self.get_response(request)

        return response
