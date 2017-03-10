from rest_framework.response import Response as djangoResponse
from rest_framework import status

class Response(object):
    """Clase para formatear el Response de la aplicacion

    Args:
        data (dict): Diccionario para el response
        status (int): Status http del response
        error (str): Mensaje de error del response
    """

    class Inner:

        def __init__(self, data, status, error):

            self.status = status
            if data: self.data = data
            if error: self.error = error

    def __new__(self, data = {}, status=status.HTTP_200_OK, error=None):

        response = self.Inner(data, status, error)

        return djangoResponse(response.__dict__, status=response.status)

