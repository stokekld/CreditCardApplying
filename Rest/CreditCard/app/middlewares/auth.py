from django.http import JsonResponse
from rest_framework import status
from app.token import Token
from jwt import DecodeError, ExpiredSignatureError
import json

class Auth(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.path_info != "/usuarios/auth":
            try:
                Token.valToken(request.META['HTTP_AUTHORIZATION'])
            except KeyError:
                return JsonResponse({'error': "El request no tiene token de autorizacion"}, status=status.HTTP_400_BAD_REQUEST)
            except (DecodeError, ExpiredSignatureError) as e:
                # print e
                return JsonResponse({'error': "El token no es valido"}, status=status.HTTP_403_FORBIDDEN)

        response = self.get_response(request)

        if request.path_info != "/usuarios/auth":
            token = Token.refresh(request.META['HTTP_AUTHORIZATION'])
            if token:
                data = response.data
                if 'data' in data:
                    data['data']['token'] = token
                else: 
                    data['data'] = {'token': token}
                return JsonResponse(data, status=response.status_code)

        return response

