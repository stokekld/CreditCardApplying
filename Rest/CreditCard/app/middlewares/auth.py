from django.http import JsonResponse
from rest_framework import status
from app.token import Token
from app.url import Urls

import json

class Auth(object):
    """Middleware para autorizacion"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # isurlauth = self.isUrlAuth(request.path_info)
        isurlauth = Urls(request.path_info).isSafe

        if not isurlauth:
            try:
                token = Token(request.META['HTTP_AUTHORIZATION'])
            except KeyError:
                return JsonResponse({'error': "El request no tiene token de autorizacion"}, status=status.HTTP_400_BAD_REQUEST)

            if not token.validate:
                return JsonResponse({'error': "El token no es valido"}, status=status.HTTP_403_FORBIDDEN)

        response = self.get_response(request)

        if not isurlauth:
            if token.refresh:
                data = response.data
                if 'data' in data:
                    data['data']['token'] = token.new
                else: 
                    data['data'] = {'token': token.new}
                return JsonResponse(data, status=response.status_code)

        return response


